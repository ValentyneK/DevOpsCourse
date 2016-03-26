#Triangle check
import math
import sys
a=float(sys.argv[1])
b=float(sys.argv[2])
c=float(sys.argv[3])
#Triangle inequality check:
if (((a+b)>c) and ((b+c)>a) and ((a+c)>b)):
	print ('triangle')
else:
	print ('not triangle')