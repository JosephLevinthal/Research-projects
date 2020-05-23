senha = int (input("Digite uma senha de 6 digitos:"))
N1 = senha%10
n2 = senha//10
N2 = n2%10
n3 = senha//100
N3 = n3%10
n4 = senha//1000
N4 = n4%10
n5 = senha//10000
N5 = n5%10
n6 = senha//100000
N6 = n6%10
if ((N1+N3+N5)%(N2+N4+N6)==0):
	print ("acesso liberado")
else:
	print ("senha invalida")


