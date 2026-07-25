#!/bin/bash

# Small bash script to recursively copy in every subdirectory the __init__.py file to treat the scripts as modules.

FILE="__init__.py"
DIR="$(pwd)"

for subdirs in $DIR; do
    find . -type d -exec cp "$FILE" {} \;
done    