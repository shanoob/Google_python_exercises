#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib
import commands

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""
def utility(dir):
  final=[]
  finallist=[]
  res=[]
  f=open(dir, 'r')
  k=re.findall(r'(GET)(\s)(\S+)(-\w+.jpg)(\s)(HTTP)', f.read())
  for i in k:
    match=re.search(r'puzzle', i[2])
    if match:
      if i not in final:
        final.append(i)
  for i in sorted(final, key=lambda x:x[3]):
    k=i[2]+i[3]
    finallist.append(k)
  for i in finallist:
    res.append("http://code.google.com"+i)
  return res



def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++

  res=utility(filename)
  for i in res:
  	print i
  

def download_images(src_dir, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
  res=utility(src_dir)
  k=0
  f=file(dest_dir+"/"+"index.html", 'w')
  f.write("<html><body>")
  for i in res:
    local_name='image'+str(k)
    print "downloading image%d" %(k)
    urllib.urlretrieve(i, os.path.join(dest_dir, local_name))
    f.write("<img src="+'"'+os.path.join(dest_dir, local_name)+'"'+">")
    k+=1
  f.write("</body></html>")
  f.close()
  cmd="xdg-open"+" "+'"'+dest_dir+"/"+"index.html"+'"'
  (status, output)=commands.getstatusoutput(cmd)
  sys.exit(1)

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[2]

  if todir:
    download_images(args[1], todir)
    
  else:
    read_urls(args[0])

if __name__ == '__main__':
  main()
