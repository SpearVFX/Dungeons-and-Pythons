#!/bin/bash

find tests/ -type f -name '*_tests.py' -printf "\n" -print0 -printf "\n" -exec python3.6 -m unittest {} \;
