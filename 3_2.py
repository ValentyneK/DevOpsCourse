import math
import sys
#stolbci
a=sys.argv[1]
#stroki
b=sys.argv[2]
#summa
c=sys.argv[3]
sign=False
#stolbcy
for i in range(1,int(a),1):
	if (i*(int(b)))==(int(c)):
		sign=True
		break
for i in range(1,int(b),1):
	if (i*(int(a)))==(int(c)):
		sign=True
		break
print (sign)