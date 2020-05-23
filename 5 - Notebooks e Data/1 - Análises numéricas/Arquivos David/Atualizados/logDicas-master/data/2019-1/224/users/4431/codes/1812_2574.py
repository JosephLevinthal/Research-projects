x=input("Digite a sneha: ")
j=0
m=0
for i in x:
	if(i.islower()):
		j=j+1
	if(i.isupper()):
		m=m+1
if(j>0)and(m>0)and(len(x)>=8):
	print("SENHA VALIDA")
else:
	print("SENHA INVALIDA")
		