#baby names test file
import re
import sys
one=[]
two=[]
dic={}
def find(filename):
	f=open(filename, 'r')
	t=f.read()
	y=re.search(r'(Popularity in )(\d+)', t)
	print y.group(2)
	k=re.findall(r'(<tr align="right"><td>)(\d+)(</td><td>)(\w+)(</td><td>)(\w+)(</td>)', t)
	#print k
	for i in k:
		dic[i[3]]=i[1]
		dic[i[5]]=i[1]
	#print dic
	o=sorted(dic.items())
	#print o
	for i in o:
		print i[0]+'--'+i[1]
		#one.append(i[3])
		#two.append(i[5])
	#resut=sorted(one+two)
	#for i in resut:
	#	print i
def main():
	d=len(sys.argv)
	p=range(d)
	print p
	for i in p[1:]:
		find(sys.argv[i])

if __name__ == '__main__':
  main()
#find("/media/New Volume/IT'S PYTHON/google/google-python-exercises/babynames/baby2008.html")