"""Tests for the follower/following comparison helpers."""

from __future__ import annotations

import unittest

from instagram_follow_cli.compare import find_non_reciprocal_following, normalize_username


class CompareTests(unittest.TestCase):
    def test_normalize_username(self) -> None:
        self.assertEqual(normalize_username(" @DaniloScimone "), "daniloscimone")

    def test_find_non_reciprocal_following(self) -> None:
        followers = ["anna", "luca", "@maria"]
        following = ["anna", "@maria", "giulia", "enzo"]

        self.assertEqual(find_non_reciprocal_following(followers, following), ["enzo", "giulia"])


if __name__ == "__main__":
    unittest.main()
