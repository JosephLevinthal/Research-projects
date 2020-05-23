senha = int(input("Senha:"))
one = senha//100000
two = (senha//10000)%10
tree = (senha//1000)%10
four = (senha//100)%10
five = (senha//10)%10
six = (senha%10)
soma1 = one+tree+five
soma2 = two+four+six
if(soma2%soma1 == 0):
	print("acesso liberado")
else:
	print("senha invalida")


