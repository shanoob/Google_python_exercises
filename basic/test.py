import sys
dic={}
r=[]
def count(filename):
	f=open(filename,'r')
	t=f.read().split()
	for i in t:
		r.append(i.upper())
	for i in r:
		if i not in dic:
			dic[i]=1
		else:
			dic[i]+=1
	print dic
count(sys.argv[1])