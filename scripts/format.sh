#!/usr/bin/env bash
set -ex

# If argument was given then format only that file, else format entire app
path=${1:-app}

# Format
black ${path}
ruff --fix  ${path}
