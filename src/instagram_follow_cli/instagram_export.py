"""Helpers for reading official Instagram data exports.

The project intentionally avoids scraping and personal API credentials.
This module reads the official export that Instagram lets the user download.
"""

from __future__ import annotations

import json
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(slots=True, frozen=True)
class InstagramExportData:
    """Followers and following usernames extracted from an export."""

    followers: list[str]
    following: list[str]


def _extract_usernames_from_json(payload: Any) -> list[str]:
    """Extract usernames from the most common Instagram export JSON shapes."""

    usernames: list[str] = []

    if isinstance(payload, list):
        for item in payload:
            if isinstance(item, dict) and "string_list_data" in item:
                string_list = item.get("string_list_data", [])
                if isinstance(string_list, list):
                    for entry in string_list:
                        if isinstance(entry, dict):
                            value = entry.get("value")
                            if isinstance(value, str) and value.strip():
                                usernames.append(value.strip())
            if isinstance(item, dict) and "title" in item:
                title = item.get("title")
                if isinstance(title, str) and title.strip():
                    usernames.append(title.strip())
            usernames.extend(_extract_usernames_from_json(item))
        return usernames

    if isinstance(payload, dict):
        if isinstance(payload.get("relationships_following"), list):
            for entry in payload["relationships_following"]:
                if isinstance(entry, dict):
                    title = entry.get("title")
                    if isinstance(title, str) and title.strip():
                        usernames.append(title.strip())
        if isinstance(payload.get("relationships_followers"), list):
            for entry in payload["relationships_followers"]:
                if isinstance(entry, dict):
                    title = entry.get("title")
                    if isinstance(title, str) and title.strip():
                        usernames.append(title.strip())

        if isinstance(payload.get("username"), str):
            usernames.append(payload["username"])

        string_list_data = payload.get("string_list_data")
        if isinstance(string_list_data, list):
            for item in string_list_data:
                if isinstance(item, dict):
                    value = item.get("value")
                    if isinstance(value, str) and value.strip():
                        usernames.append(value.strip())

        for key in ("relationships_followers", "relationships_following", "followers", "following"):
            nested = payload.get(key)
            if nested is not None:
                usernames.extend(_extract_usernames_from_json(nested))

    return usernames


def _load_json_from_text(text: str) -> Any:
    return json.loads(text)


def _load_file_contents(path: Path) -> Any:
    text = path.read_text(encoding="utf-8")
    return _load_json_from_text(text)


def _normalize_username(username: str) -> str:
    return username.strip().removeprefix("@").casefold()


def _deduplicate(usernames: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for username in usernames:
        normalized = _normalize_username(username)
        if normalized and normalized not in seen:
            seen.add(normalized)
            result.append(normalized)
    return result


def _read_json_candidates_from_directory(directory: Path) -> tuple[list[str], list[str]]:
    followers: list[str] = []
    following: list[str] = []

    for path in directory.rglob("*.json"):
        lower_name = path.name.lower()
        try:
            payload = _load_file_contents(path)
        except (OSError, json.JSONDecodeError):
            continue

        extracted = _extract_usernames_from_json(payload)
        if "follower" in lower_name:
            followers.extend(extracted)
        elif "following" in lower_name:
            following.extend(extracted)

    return _deduplicate(followers), _deduplicate(following)


def _read_json_candidates_from_zip(archive: Path) -> tuple[list[str], list[str]]:
    followers: list[str] = []
    following: list[str] = []

    with zipfile.ZipFile(archive) as zip_file:
        for info in zip_file.infolist():
            lower_name = info.filename.lower()
            if not lower_name.endswith(".json"):
                continue

            try:
                with zip_file.open(info) as handle:
                    payload = json.loads(handle.read().decode("utf-8"))
            except (OSError, UnicodeDecodeError, json.JSONDecodeError):
                continue

            extracted = _extract_usernames_from_json(payload)
            if "follower" in lower_name:
                followers.extend(extracted)
            elif "following" in lower_name:
                following.extend(extracted)

    return _deduplicate(followers), _deduplicate(following)


def load_export_data(source: str) -> InstagramExportData:
    """Load followers and following from an official Instagram export.

    The source can be a zip archive or an extracted folder containing JSON
    files from Instagram's "Download your information" export.
    """

    path = Path(source).expanduser().resolve()
    if not path.exists():
        raise FileNotFoundError(f"Percorso non trovato: {path}")

    if path.is_dir():
        followers, following = _read_json_candidates_from_directory(path)
    elif path.suffix.lower() == ".zip":
        followers, following = _read_json_candidates_from_zip(path)
    elif path.suffix.lower() == ".json":
        payload = _load_file_contents(path)
        extracted = _extract_usernames_from_json(payload)
        lower_name = path.name.lower()
        if "follower" in lower_name:
            followers, following = _deduplicate(extracted), []
        elif "following" in lower_name:
            followers, following = [], _deduplicate(extracted)
        else:
            followers, following = [], []
    else:
        raise ValueError("Supportati solo file .zip, cartelle estratte o file .json dell'export Instagram.")

    if not followers and not following:
        raise ValueError(
            "Nessun dato trovato nell'export. Controlla che sia il download ufficiale Instagram con follower e following.",
        )

    return InstagramExportData(followers=followers, following=following)
