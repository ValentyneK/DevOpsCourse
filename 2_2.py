import math
import sys
z=sys.argv
a=''
length=len(z)-1

while length!=0:
	a=a+z[length]
	a=a+' '
	length-=1
print (a[:-1])
