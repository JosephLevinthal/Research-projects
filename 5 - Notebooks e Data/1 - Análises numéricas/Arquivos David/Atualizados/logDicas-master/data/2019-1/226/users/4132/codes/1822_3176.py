s = input("Digite: ")

s =s.lower()
aux=0
for i in range(len(s)):
	if s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u":
		aux +=1
print(aux)
print(len(s)-aux)
