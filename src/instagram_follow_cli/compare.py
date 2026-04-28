"""Utilities for comparing Instagram follower and following lists."""

from __future__ import annotations

from typing import Iterable


def normalize_username(username: str) -> str:
    """Normalize an Instagram username for comparison."""

    return username.strip().removeprefix("@").casefold()


def find_non_reciprocal_following(
    followers: Iterable[str],
    following: Iterable[str],
) -> list[str]:
    """Return usernames that are followed but do not follow back.

    The result is sorted for stable output.
    """

    followers_set = {normalize_username(username) for username in followers}
    non_reciprocal = {
        normalize_username(username)
        for username in following
        if normalize_username(username) not in followers_set
    }
    return sorted(non_reciprocal)
