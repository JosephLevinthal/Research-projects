from numpy import*
a=array(eval(input("quantidade de jogadas de eusapia: ")))
b=array(eval(input("quantidade de jogadas de barsanulfo: ")))
#variavel contadora 
qr=0 #quantidade de rodadas
va=0 #vitorias de eusapia 
vb=0 #vitorias de barsanulfo 
while ( size(a) > qr < size (b) ):
	if ( a[qr] == b[qr] ):
		va = va
		vb = vb
	elif ( a[qr] == 11 and b[qr] == 33 ) or ( a[qr] == 22 and b[qr] == 11 ) or ( a[qr] == 33 and b[qr] == 22 ):
		va += 1
	elif ( b[qr] == 11 and a[qr] == 33 ) or ( b[qr] == 22 and a[qr] == 11 ) or ( b[qr] == 33 and a[qr] == 22 ):
		vb += 1 
	qr = qr + 1
print(qr)
if ( va == vb ):
	print("EMPATE")
elif ( va > vb ):
	print("EUSAPIA")
else:
	print("BARSANULFO")
