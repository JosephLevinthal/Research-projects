#Digitar a idade
x = int(input("digite a idade do cliente: "))

#utilizando condições if e else
if (x>=18):
	idade = "eleitor"
else:
	idade = "nao_eleitor"
	
#imprimir o resultado
print(idade)