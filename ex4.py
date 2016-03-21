import math
import sys
x = int(sys.argv[1])
a=0
b=1
c=0
round=x
if x==0:
	print (a)
elif x==1:
	print (b)
elif x>1:
	while round>1:
		c=a+b
		a=b
		b=c
		#print (a, b)
		round=round-1
	print (c)
