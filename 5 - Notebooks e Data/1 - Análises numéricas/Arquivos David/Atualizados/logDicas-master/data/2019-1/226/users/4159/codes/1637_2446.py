senha = int(input("senha: "))
a = senha//100000
b = (senha%100000)//10000
c = (senha%10000)//1000
d = (senha%1000)//100
e = (senha%100)//10
f = senha%10
if((b+d+f)%(a+c+e)!= 0):
	print("senha invalida")
else:
	print("acesso liberado")