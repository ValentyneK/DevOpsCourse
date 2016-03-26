import math
import sys
a=sys.argv[1]
a=a.replace(' ', '')
b=''
word=''
leng=len(a)
gr=len(a)//5
#print (gr)
buff=''
dict = {"aaaaa":"a","aaaab":"b","aaabb":"c","aabbb":"d","abbbb":"e","bbbbb":"f","bbbba":"g","bbbab":"h","bbabb":"i","babbb":"j","abbba":"k","bbbaa":"l","bbaab":"m","baabb":"n","aabba":"o","abbab":"p","bbaba":"q","babab":"r","ababb":"s","babba":"t","abbaa":"u","bbaaa":"v","baaab":"w","aaaba":"x","aabab":"y","aabaa":"z"}
for i in range(0,len(a),1):
	if a[i].islower():
		b=b+'a'
	else:
		b=b+'b'
#print (b)
b=b[0:(len(a)-(len(a)-((((len(a)))//5)*5)))]
#print (b)

for i in range(0,(len(b)),5):
	buff=b[i]+b[i+1]+b[i+2]+b[i+3]+b[i+4]
	#print (buff)
	#print (dict.get(str(buff)))
	word=word+(dict[buff])
	#print (dict[buff])
	#print (buff)
print (word)


