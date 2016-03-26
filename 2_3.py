import math
import sys
z=sys.argv[1]
s=0
l=len(z)-1
op=0
while (s<=l) & (op>=0):
	if z[s]=='(':
		op+=1
	elif z[s]==')':
		op-=1
	s+=1
if op==0:
	print ('YES')
else:
	print ('NO')