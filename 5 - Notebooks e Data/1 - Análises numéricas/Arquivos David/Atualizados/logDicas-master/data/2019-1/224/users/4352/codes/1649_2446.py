senha = int(input("digite sua senha: "))
s1 = senha//100000%10000%1000%100%10
s2 = senha//10000%1000%100%10
s3 = senha//1000%100%10
s4 = senha//100%10
s5 = senha//10%10
s6 = senha%10

calculo1 = s2 + s4 + s6 
calculo2 = s1 + s3 + s5

if calculo1 % calculo2 == 0: 
	print("acesso liberado")
else:
	print("senha invalida")
