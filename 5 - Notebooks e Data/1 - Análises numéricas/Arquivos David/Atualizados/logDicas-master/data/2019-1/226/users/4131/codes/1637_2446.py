senha = int(input("senha:"))
d1 = senha//100000
d2 = (senha//10000)%10
d3 = (senha//1000)%10
d4 = (senha//100)%10
d5 = (senha//10)%10
d6 = senha%10
if((d2+d4+d6)%(d1+d3+d5)!=0 ):
	print("senha invalida")
else:
	print("acesso liberado")