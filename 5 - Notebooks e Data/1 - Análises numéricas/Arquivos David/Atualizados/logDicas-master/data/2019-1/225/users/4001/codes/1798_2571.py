S = input("String: ")

v = ""
for i in range(len(S)):
	if (S[i].upper() != "A"):
		v = v + S[i]
	elif (S[i].upper() == "A"):
		v = v 
print(v)
		
		