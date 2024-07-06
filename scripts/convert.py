#!/usr/bin/env python3

# import re
# 
# lines = input()
# 
# for line in lines.splitlines():
#     result = re.findall(r'(.*):(\d+):(\d+): (.*)', line)[0]
#     print(f"::error file={result[0]},line={result[1]},col={result[2]},title=flake8::{result[3]}")

print("::error file=app.py,line=1,col=5::Missing semicolon")
