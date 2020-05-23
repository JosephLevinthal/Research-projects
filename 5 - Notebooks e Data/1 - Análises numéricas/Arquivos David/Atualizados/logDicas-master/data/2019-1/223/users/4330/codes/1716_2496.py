a=int(input("digite um numero: "))

soma = a
#variavel acumuladora
total = 0

while ( a != -1 ):
	a = int(input("digite um numero: "))
	soma = soma + a
	total = a + soma
	
	if ( a == -1):
		print( total + 1 + 1)
