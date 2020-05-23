n = int(input("Digite um texto: "))
pi = 0
while ( n >= 1 ):
	if ( (n % 2) == 1 ):
		#impar
		pi = pi + ( 4 /( 2 * n -1))
	else:
		#par
		pi = pi - ( 4 / ( 2 * n -1))
		
	n = n - 1 # n = 2
print(round(pi,8))
