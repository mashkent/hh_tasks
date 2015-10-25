#!/usr/bin/env python

from statistics import median
# http://bonsai.hgc.jp/~mdehoon/software/python/Statistics/

firstStr = []
for x in raw_input().split():
    firstStr.append(float(x))

secondStr = []
for x in raw_input().split():
    secondStr.append(float(x))

print median(firstStr + secondStr)

