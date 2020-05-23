from numpy import *

s = input("hcsdchsv: ").upper()
s = s.replace(' ',' ')

hdtv= ""
i= -1
b= 1
c= 0

while (i >= -len(s)):
	hdtv = hdtv + s[i]
	if(s[c]) != (s[i]):
		b= 0 
	c = c + 1
	i= i - 1
	
print(s)
print(b)