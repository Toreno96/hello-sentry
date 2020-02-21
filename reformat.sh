#!/usr/bin/env bash

autoflake . \
    --remove-all-unused-imports \
    --recursive \
    --remove-unused-variables \
    --in-place
isort . \
    --multi-line=3 \
    --trailing-comma \
    --force-grid-wrap=0 \
    --combine-as \
    --line-width 120 \
    --recursive \
    --apply
black .
