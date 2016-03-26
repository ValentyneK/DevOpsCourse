import math
import sys
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])
k = str("la")
if x==1:
	k="la"
elif x>1:
	k=k+"-"
	k*=x
	k=k[0:-1]
Goat=str("Everybody sing a song:")
if y==0:
	Goat=Goat
elif y>0:
	k=k+" "
	k=k*y
	k=k[0:-1]
	Goat+=" "
	Goat=Goat+k
	
if z==1:
	Goat+="!"
elif z==0:
	Goat+="."

print (Goat)
