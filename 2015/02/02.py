#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""02.py - https://adventofcode.com/2015/day/2"""


def main():
    """main"""
    floor = 0
    with open("input.txt") as f:
        l = f.readline()
        for c in l:
            if c == '(':
                floor += 1
            else:
                floor -= 1
        
        print(floor)


if __name__ == '__main__':
    main()
