from numpy import *
s = input("String: ")

i = 0
k = 3
msg = ""

while(i<len(s)):
	if(i==(len(s)-3)):
		msg = msg + s[i:k]
		i = i+3
		k=k+3
	else:
		msg=msg+s[i:k]+ "."
		i = i + 3
		k = k + 3
print(msg)
		
		
		