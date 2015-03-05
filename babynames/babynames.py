#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

#run this program as
#python babynames.py "baby1996.html" "baby2000.html"
#or
#python babynames.py '--summaryfile' "baby1996.html" "baby2000.html"



import sys
import re
import os

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""
def utility(filename):
  dic={}
  f=open(filename, 'r')
  t=f.read()
  y=re.search(r'(Popularity in )(\d+)', t)
  res=[y.group(2)]
  k=re.findall(r'(<tr align="right"><td>)(\d+)(</td><td>)(\w+)(</td><td>)(\w+)(</td>)', t)
  #print k
  for i in k:
    dic[i[3]]=i[1]
    dic[i[5]]=i[1]
    #print dic
  o=sorted(dic.items())
  #print o
  for i in o:
    res.append(i[0]+' '+i[1])
  return res

def extract_names(filename):
  res=utility(filename)
  for i in res:
    print i
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++

  for i in args:
    names = utility(i)

    # Make text out of the whole list
    #text = '\n'.join(names)

    if summary:
      t=os.path.basename(i)

      outfile = open(t+".summary.txt", 'w')
      for i in names:
        outfile.write(i + '\n')
      outfile.close()
    else:
      for i in names:
        print i
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':
  main()
