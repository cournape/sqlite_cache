#! /bin/sh
set -e
coverage erase
coverage run --branch --source=sqlite_cache -m haas  sqlite_cache
coverage report --include=sqlite_cache/* -m
