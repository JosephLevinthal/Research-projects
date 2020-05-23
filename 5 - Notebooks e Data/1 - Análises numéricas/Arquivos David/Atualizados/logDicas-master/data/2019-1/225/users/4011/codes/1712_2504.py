q1 = int(input("Quantidade inicial de virus no sangue: "))
q2 = int(input("Quantidade inicial de leucocitos no sangue: "))
p1 = int(input("Percentual diaria do virus: "))/100
p2 = int(input("Percentual diaria do leucocitos: "))/100

dias = 0
c1 = q1
c2 = q2

while ( c2 < 2*c1 ):
	
	c2 = c2 + ( c2*p2 )
	c1 = c1 + ( c1*p1 )
	dias = dias + 1
	
print( dias )