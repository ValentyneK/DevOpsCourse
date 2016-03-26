import math
import sys
a = str(sys.argv[1])
a=a.replace(' ', '')
a=a.lower()

ispoly=False
l=len(a)-1
s=0

while s<l:
	if a[s]==a[l]:
		ispoly=True
		s+=1
		l-=1
	else:
		ispoly=False
		break
if ispoly==True:
	print ('YES!')
else:
	print ('NO!')