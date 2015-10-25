#!/usr/bin/env python

import sys
import math

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
precision = 8 # limitation on the size of fractional part
delimiter = '.'

def principal_period(s): # function finds period of string if it is repeated (for example, '121212' -> '12')
  i = (s+s).find(s, 1, -1)
  return None if i == -1 else s[:i]

def if_periodical(inputStr): # function checks string subsequently removing first symbols
  pos = 0 # position where starts periodical part
  period = ''
  s = inputStr
  while len(s) > 3:
    period = principal_period(s)
    if period is None: # it could be if there is a preperiod or no period at all
      s = s[1:]
      pos += 1
    else:
      break
  return (period, pos)

def simplify_periodical_fraction(inputStr):
  if len(inputStr) < precision:
    return inputStr
  else:
    period, pos = if_periodical(inputStr)
    if period is None:
      return inputStr
    else:
      return inputStr[:pos] + '(' + period + ')' # return preperiod part of string + "(period part of string)"

def convertIntPart(intPart, base): # function converts integer part of decimal number into numsystem with base
  intRes = ''
  while intPart >= base:
    intRes += digits[intPart % base]
    intPart = intPart // base
  intRes += digits[intPart]
  return intRes[::-1]

def convertFracPart(fracPart, base): # function converts fractional part of decimal number into numsystem with base
  iterations = 0
  fracRes = ''
  while fracPart * base != 0 and iterations < precision:
    fracPart, newintPart = math.modf(fracPart * base)
    fracRes += digits[int(newintPart)]
    iterations += 1
  return fracRes

def fromDecimaltoBase(number, base): # function converts decimal number to numsystem with base
  fracPart, intPart = math.modf(number)    
  return convertIntPart(int(intPart), base) + delimiter + simplify_periodical_fraction(convertFracPart(fracPart, base))

def main():
  if len(sys.argv) != 4:
    sys.stderr.write("Error! Three numbers must be entered. Example: 1 12 10 \n")
    return 1
  else:
     print fromDecimaltoBase(float(sys.argv[1]) / float(sys.argv[2]), int(sys.argv[3]))

main()
