m = int(input("Insira um numero:"))

po = 0
soma = 0


while(m != 0):
	soma = m + soma
	m = int(input("Insira um numero:"))
if(soma > 0):
	print(soma)
	print("Acima")
elif(soma < 0):
	print(soma)
	print("Abaixo")
else:
	print(soma)
	print("Inicial")