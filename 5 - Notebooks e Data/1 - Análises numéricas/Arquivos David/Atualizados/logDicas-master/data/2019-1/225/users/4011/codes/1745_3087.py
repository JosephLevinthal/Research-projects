n = int(input("Numeros inteiros: "))
d1 = 0
d2 = 0
soma1 = 0
soma2 = 0

while( n != 0):
	if( n%2 == 0):
		
		d1 = d1 + 1
		soma1 = soma1 + n 
		n = int(input("Numeros inteiros: "))
		
	else:
		d2 = d2 + 1
		soma2 = soma2 + n
		n = int(input("Numeros inteiros: "))

print(round(soma1/d1, 1))
print(round(soma2/d2, 1))