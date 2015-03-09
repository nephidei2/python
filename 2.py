#!/usr/bin/python
from __future__ import division
from decimal import Decimal

def norm(p_val, vector_string):
    vector_els = [pow(abs((float(el))), p_val) for el in vector_string.split(' ')]
    return pow(sum(vector_els), (float(Decimal(1))/p_val))

def main():
    p_val = (float(raw_input()))
    vector = str(raw_input())
    print int(norm(p_val, vector))

if __name__ == '__main__':
    main()

