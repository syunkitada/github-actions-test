#!/usr/bin/env python3

import re
import sys

lines = sys.stdin.readlines()

for line in lines:
    result = re.findall(r"(.*):(\d+):(\d+): (.*)", line)
    if len(result) > 0:
        result = result[0]
        print(
            f"::error file={result[0]},line={result[1]},col={result[2]},title=flake8::{result[3]}"
        )
