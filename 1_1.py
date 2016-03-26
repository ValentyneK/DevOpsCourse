import math
import sys
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])
x =   (1 / (c*math.sqrt(2*math.pi)))  * math.exp( -( ((a-b)**2) / (2*(c**2))) ) 
#((math.sqrt(a * b)) / (math.exp(a) * b)) + (a * (math.exp (2 * a / b)))
print (x)