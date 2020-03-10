#!/usr/bin/env sh

poetry export -f requirements.txt -o openreservation/requirements.txt  --without-hashes

