#!/bin/sh
poetry config virtualenvs.create false
poetry install --no-root

exec "$@"
