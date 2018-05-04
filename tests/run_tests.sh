#!/bin/bash

find tests/ -type f -name '*_tests.py' -exec python3.6 -m unittest {} +
