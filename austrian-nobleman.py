#!/usr/bin/env python3

import sys

def eprint(*args, **kwargs):
  print(*args, file=sys.stderr, **kwargs)

debug = False

def dprint(*args, **kwargs):
  if debug: eprint(*args, **kwargs)

source_string = ""
index = 0
line = 1

def lex_string():
  global index
  current_token = "\""
  while(index<len(source_string)):
    c = source_string[index]
    index+=1

    if c == '"':
      current_token+=(c)
      return current_token
    if c == '\\': #skip over any \"s that might occur
      current_token+=(c)
      index+=1
      current_token+=(source_string[index])
    if c == '\n':
      eprint("String literal unterminated by end of line", line)
      exit()
    else:
      current_token+=(c)

def lex_char(): #technically multicharacter char literals aren't in the standard, but some compilers accept them.
  global index
  current_token = "\'"
  while(index<len(source_string)):
    c = source_string[index]
    index+=1

    if c == '\'':
      current_token+=(c)
      return current_token
    if c == '\\':
      current_token+=(c)
      index+=1
      current_token+=(source_string[index])
    if c == '\n':
      eprint("Character literal unterminated by end of line", line)
      exit()
    else:
      current_token+=(c)


#TODO: track char number, and use to eprint errors if need be
def lex():
  global index
  global line
  ast = []
  current_token = ""
  while(index<len(source_string)):
    c = source_string[index]
    index+=1
    
    if c.isspace() or c == '"' or c == '\'' or c == '[' or c == ']':
      if current_token:
        ast.append(current_token)
        current_token = ""
    
    if c == ']':
      return ast
    elif c == '[':
      ast.append(lex())
    elif c == '"':
      ast.append(lex_string())
    elif c == '\'':
      ast.append(lex_char())
    elif not c.isspace():
      current_token+=(c)

    if c=="\n": line+=1
  return ast
    

def ast_to_c(ast):
  return ast #TODO: actually interpret this
	
def main():
  with open(sys.argv[1],"r") as file:
    global source_string
    s=file.readlines()
    source_string = "".join([i for i in s if i[:2] != "#!"]) #we must honor the holy shebang... by stripping it.
    print(ast_to_c(lex()))

main()