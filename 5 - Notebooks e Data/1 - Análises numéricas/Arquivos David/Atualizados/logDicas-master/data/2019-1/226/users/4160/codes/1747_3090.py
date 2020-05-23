m = int(input("Movimentos da lagartixa: "))
i = 0

soma = 0

while (m != 0):
	m = int(input("Movimentos da lagartixa: "))
	soma = soma + m
	i = i + 1
print(soma)
if(soma > 0):
	print("Acima")
if(soma < 0 and soma !=0):
	print("Abaixo")
if(m == i):	
	print("Inicial")
