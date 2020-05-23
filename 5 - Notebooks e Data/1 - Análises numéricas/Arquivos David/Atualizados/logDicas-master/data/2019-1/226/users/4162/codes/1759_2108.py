s=input("digite uma string: ").lower()
a=""
c=s.replace(" ","")
i=0
j=1
while i!=len(c):
	b=c[i:j]
	if b!="a" and b!="e" and b!="i" and b!="o" and b!="u":
		b="p"
	a=a+b
	i=i+1
	j=j+1
print(a)