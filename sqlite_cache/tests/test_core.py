from __future__ import absolute_import

import sys
import time

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

from ..core import SQLiteCache


class TestCore(unittest.TestCase):
    def test_simple(self):
        # Given
        cache = SQLiteCache(":memory:")
        key = "nono"
        value = "le petit robot"

        # When
        cache.set(key, value)

        # Then
        self.assertEqual(cache.get(key), value)
        cache.close()

    def test_size(self):
        # Given
        capacity = 3
        cache = SQLiteCache(":memory:", capacity=capacity)

        # When/Given
        cache.set("1", "one")
        self.assertEqual(cache.size(), 1)

        # When/Given
        cache.set("2", "two")
        self.assertEqual(cache.size(), 2)

        # When/Given
        cache.set("3", "three")
        self.assertEqual(cache.size(), 3)

        # When/Given
        cache.set("4", "four")
        self.assertEqual(cache.size(), 3)

        cache.close()

    def test_delete(self):
        # Given
        cache = SQLiteCache(":memory:")

        # When
        cache.set("1", "2")

        # Then
        self.assertEqual(cache.get("1"), "2")

        # When
        cache.delete("1")

        # Then
        self.assertIsNone(cache.get("1"))

        cache.close()

    def test_age(self):
        # Given
        capacity = 2
        cache = SQLiteCache(":memory:", capacity=capacity)

        # When
        cache.set("1", "1")
        time.sleep(0.1)
        cache.set("2", "2")
        time.sleep(0.1)
        cache.set("3", "3")

        # Then
        self.assertEqual(cache.size(), capacity)
        self.assertEqual(cache.get("2"), "2")
        self.assertEqual(cache.get("3"), "3")
        self.assertIsNone(cache.get("1"))

        cache.close()

    def test_context_manager(self):
        with SQLiteCache(":memory:") as cache:
            self.assertFalse(cache.closed)
        self.assertTrue(cache.closed)

    def test_overwrite(self):
        # Given
        cache = SQLiteCache(":memory:")
        key = "nono"
        value = "le petit robot"

        # When/Then
        cache.set(key, "themis")
        self.assertEqual(cache.get(key), "themis")

        # When/Then
        cache.set(key, value)
        self.assertEqual(cache.get(key), value)

        cache.close()
