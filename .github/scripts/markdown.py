#!/usr/bin/python

import sys
import markdown2

def main():
    with open(sys.argv[1], 'r') as file:
        data = file.read()
        print(markdown2.markdown(data, extras=["fenced-code-blocks", "full_yaml_metadata"]))

main()