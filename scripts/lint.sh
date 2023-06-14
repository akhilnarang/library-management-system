#!/usr/bin/env bash

set -ex

# If argument was given then lint only that file, else lint entire app
path=${1:-app}

# Lint
mypy $path --explicit-package-bases
black $path --check
ruff $path --diff