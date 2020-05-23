senha=int(input("entre com a senha: "))

term1=senha//100000
term2= (senha%100000)//10000
term3= (senha%10000)//1000
term4= (senha%1000)//100
term5= (senha%100)//10
term6= senha%10

if((term2+term4+term6)%(term1+term3+term5)==0):

	print("acesso liberado")
	
else:
	print("senha invalida")