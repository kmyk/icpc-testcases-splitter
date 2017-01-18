#!/bin/bash
cd "$(git rev-parse --show-toplevel)"/example
g++ a.cpp
python3 ../split.py ./a.out -i in.txt -o out-{}.txt --footer '0 0\n'
