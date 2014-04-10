.. image:: https://travis-ci.org/cournape/sqlite_cache.png
   :target: https://travis-ci.org/cournape/sqlite_cache

.. image:: https://coveralls.io/repos/cournape/sqlite_cache/badge.png?branch=master
   :target: https://coveralls.io/r/cournape/sqlite_cache?branch=master

A dumb cache backed by sqlite. The cache has a max capacity and will delete
older entries to make space for new entries.

Example of usage::

    from sqlite_cache import SQLiteCache

    cache = SQLiteCache(".cache.db")
    cache.set("key", "value")

    print "value for {0!r} is {0!r}".format("key", cache.get("key"))

Python >= 2.6 and >= 3.2 are supported.
