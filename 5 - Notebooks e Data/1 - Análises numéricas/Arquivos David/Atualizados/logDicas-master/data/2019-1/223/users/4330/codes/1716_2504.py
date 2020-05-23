#qic=int(input("Qunatidade inicial de copias: "))
#qil=int(input("Quantidade inical de leucocitos: "))
#pmv=int(input("percentual de multiplicaçao do virus: "))
#pml=int(input("percentual de multiplicaçao dos leucocitos: "))

#variavel acumuladora
qic=int(input("Qunatidade inicial de copias: "))
qil=int(input("Quantidade inical de leucocitos: "))#varia
pmv=int(input("percentual de multiplicacao do virus: "))
pml=int(input("percentual de multiplicacao dos leucocitos: "))

#variavel contadora
d = 0

while ( qic > qil/2 ):
	qic =  qic + ( qic * ( pmv/100) )
	qil =  qil + ( qil * ( pml/100) ) 
	d = d + 1
print(d)

