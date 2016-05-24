#!/usr/bin/python

from random import randint
import os

for range_int in range(5):
  random_int = randint(0,100)
  os.system("touch %s-%s.txt" % (range_int, random_int))
