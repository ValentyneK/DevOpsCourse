import math
import sys
a=sys.argv[1]
b=sys.argv[2]
hsum, lsum, count=0, 0, 0
while (int(a))<(int(b)):
	if len(str(a))<6:
		a=(('0')*(6-(len(str(a)))))+str(a)
	hsum=(int(a[0]))+(int(a[1]))+(int(a[2]))
	lsum=(int(a[-1]))+(int(a[-2]))+(int(a[-3]))
	if hsum==lsum:
		count+=1
	hsum=(int(hsum))*0
	lsum=(int(lsum))*0
	a=(int(a))+1
	a=str(a)
#print ((str(count)),a, sep=', ', end='.')
print (str(count))