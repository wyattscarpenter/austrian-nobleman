#!/usr/bin/env python3

import sys

def eprint(*args, **kwargs):
  print(*args, file=sys.stderr, **kwargs)

debug = False

def dprint(*args, **kwargs):
  if debug: eprint(*args, **kwargs)

#TODO: track line and char number, and use those to eprint errors if need be
def an_to_c(string):
  pass
	

with open(sys.argv[1],"r") as file:
  s=file.readlines()
  s = "".join([i for i in s if i[:2] != "#!"]) #we must honor the holy shebang... by stripping it.
  print(s)

