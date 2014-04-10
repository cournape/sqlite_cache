#! /bin/sh
set -e
coverage erase
coverage run --branch -m haas  sqlite_cache
coverage report --include=sqlite_cache/* -m
