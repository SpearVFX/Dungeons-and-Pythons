#!/bin/bash

PYTHONPATH="${PYTHONPATH}:${pwd}:$(pwd)/src"
export PYTHONPATH

chmod +x "$(pwd)/src/tests/run_tests.sh"

find ./ -type f -name '*_tests.py' -exec python3.6 {} \;
