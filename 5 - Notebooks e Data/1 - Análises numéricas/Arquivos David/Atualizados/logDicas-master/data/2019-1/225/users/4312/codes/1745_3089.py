x = int(input("Insira um numero: "))
soma = 0
x = x
while(x != 0):
	soma = soma + x
	x = int(input("insira um numero: "))

print(soma)	
if(soma > 0):
	soma = "Direita"
elif(soma == 0):
	soma = "Inicial"
else:
	soma = "Esquerda"
print(soma)