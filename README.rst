A dumb cache backed by sqlite. The cache has a max capacity and will delete
older entries to make space for new entries.

Example of usage::

    from sqlite_cache import SQLiteCache

    cache = SQLiteCache(".cache.db")
    cache.set("key", "value")

    print "value for {0!r} is {0!r}".format("key", cache.get("key"))
