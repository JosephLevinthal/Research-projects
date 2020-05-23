cn=str(input("insira caracteres numericos: "))
co=""
c=0
i=0
j=3

while c!=len(cn):
	a=cn[i:j]
	co=co+a+'.'
	i=i+3
	j=j+3
	c=3+c
print(co[:-1])