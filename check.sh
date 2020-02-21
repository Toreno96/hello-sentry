#!/usr/bin/env bash

flake8 || exit 1
black --check --quiet . || { echo 'ERROR: code is unformatted; perhaps use the `reformat.sh` script'; exit 1; }
