from setuptools import setup

if __name__ == "__main__":
    setup(name="sqlite_cache",
          version="0.0.4.dev1",
          author="David Cournapeau",
          packages=["sqlite_cache", "sqlite_cache.tests"],
          license="BSD")
