#Missing card
import math
import sys
i, j=0, 0
z=sys.argv
z=z[1:]
z=''.join(str(e) for e in z)
#print ("Total cards:",z[0])
sign=False
for i in range(1,(int(z[0])+1),1):
	#print ("Round starts:",i)
	for j in range (1,len(z),1):
		#print ('check')
		if i==(int(z[j])):
			#print (i, "equals", z[j])
			sign=True
	if sign==False:
		print ("Missing card is #" , i)
		break
	else:
		#print ("Round finished:" , i)
		sign=False