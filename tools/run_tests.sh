#! /bin/sh
set -e
coverage erase
coverage run --branch -m nose.core  sqlite_cache
coverage report --include=sqlite_cache/* -m
