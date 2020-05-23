from numpy import*
mf = array(eval(input("Digite: ")))

while(size(mf) > 1):

	aprovados = 0
	
	for elemento in mf:
		if( 5 <= elemento < 7 ):
			aprovados = aprovados + 1
			
	print(aprovados)
	
	mf = array(eval(input("Digite novamente: ")))
