s=input("digite a frase: ")
i=0
f=""
for elemento in s:
	if(s[i]!="a" and s[i]!="A"):
		f=f+s[i]
	else:
		j=s.replace("a", "")
	i=i+1
print(f)
	