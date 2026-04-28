"""Official Instagram API integration points.

This module intentionally contains stubs only. Replace the TODOs with the
official authentication and data access flow supported by Instagram.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence


@dataclass(slots=True)
class InstagramAccount:
    """Minimal account representation returned by the official API."""

    username: str
    is_private: bool


class InstagramApiError(RuntimeError):
    """Base error for Instagram API integration failures."""


class AuthenticationRequiredError(InstagramApiError):
    """Raised when an action requires a logged-in user session."""


class PrivateAccountError(InstagramApiError):
    """Raised when the target account requires authorization."""


def authenticate() -> None:
    """Authenticate the current user via the official Instagram flow.

    TODO: implement the official login and authorization flow.
    """

    raise NotImplementedError("Official Instagram authentication is not implemented yet.")


def fetch_followers(username: str) -> Sequence[str]:
    """Fetch the follower list for a given username.

    TODO: call the official Instagram API and handle pagination.
    """

    raise NotImplementedError("Fetching Instagram followers is not implemented yet.")


def fetch_following(username: str) -> Sequence[str]:
    """Fetch the following list for a given username.

    TODO: call the official Instagram API and handle pagination.
    """

    raise NotImplementedError("Fetching Instagram following is not implemented yet.")
