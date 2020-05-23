q1 = int(input("Quantidade inicial de tambaquis: "))
p1 = float(input("Percentual de crescimento anual da quantidade de tambaquis: "))/100
q2 = int(input("Quantidade de tambaquis retirados apos a venda: "))

max1 = 12000
anos = 0
c1 = q1
c2 = q2

while( c1 > 0 and c1 < max1 ):
	
	c2 = q2
	c1 = c1 + ( c1* p1 ) - c2
	anos = anos + 1
	

if( c1 >= max1):
	print("LIMITE")
	print( anos )
else:
	print("EXTINCAO")
	print( anos )