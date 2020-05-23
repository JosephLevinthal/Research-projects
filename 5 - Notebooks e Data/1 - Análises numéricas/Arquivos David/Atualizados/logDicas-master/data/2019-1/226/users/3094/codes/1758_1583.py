v = input("")

i = 0
k = 3
msg = ""

while(i < len(v)):
	if(i == (len(v) - 3)):
		msg = msg + v[i:k]
		i = i+ 3
		k = k + 3 
	else:
		msg = msg + v[i:k] + "."
		i = i + 3 
		k = k + 3
print(msg)