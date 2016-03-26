import math
import sys
x=sys.argv[1]
p=sys.argv[2]
y=sys.argv[3]
x, p, y, sum=float(x), float(p), float(y), x
proc=p/100
count=0
while sum<y:
	sum=round((sum+(sum*proc)),2)
	count+=1
print (count)