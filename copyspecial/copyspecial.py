#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

def utility(dir):
  l=[]
  t=os.listdir(dir)
  for i in t:
    match=re.search(r'__(\w+)__', i)
    if match:
      l.append(os.path.abspath(i))
  return l

def get_special_paths(dir):
  res=utility(dir)
  for i in res:
    print i


def copy_to(paths, todir):
  #for i in paths:
    res=utility(paths)
    print res
    if len(res)==0:
      print "no special content to copy..!!"
    else:
      for i in res:
        if os.path.isdir(todir):
          #print "directory already available, copying the contents to it \n"
          shutil.copy(i, todir)
        else:
          os.mkdir(todir)
          #print "directory created at: ", todir, "\n"
          shutil.copy(i, todir)
      print "copied"

  #print "done"
def zip_to(dir):
  res=utility(dir)
  command="zip -j zipfile"
  for i in res:
    command=command+' '+'"'+i+'"'
  #print command
  (status, output) = commands.getstatusoutput(command)
  print "status is: ", status
  print "output is: \n", output
# +++your code here+++
# Write functions and modify main() to call them



def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  #print get_special_paths(sys.argv[2])
  #paths=["/media/New Volume/IT'S PYTHON/google/google-python-exercises/copyspecial","/media/New Volume/IT'S PYTHON/google/google-python-exercises/basic"]
  #copy_to(sys.argv[2])
  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  if args[0] == '--todir':
    copy_to(args[2], args[1])

  if args[0] == '--tozip':
    zip_to(args[1])

  if args[0] != '--tozip' and args[0] != '--todir':
    get_special_paths(args[0])
   # del args[0:2]

  

  # +++your code here+++
  #if todir:
   # copy_to(args,todir)
  #elif tozip:
    #zip_to(args, tozip)
  #else:
   # for i in args:
    #  print get_special_paths(i)
  # Call your functions
  
if __name__ == "__main__":
  main()
