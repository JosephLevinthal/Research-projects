from numpy import*
b = array([[0,2,11,6,15,11,1],
			 [2,0,7,12,4,2,15],
			 [11,7,0,11,8,3,13],
			 [6,12,11,0,10,2,1],
			 [15,4,8,10,0,5,13],
			 [11,2,3,2,5,0,14],
			 [1,15,13,1,13,14,0]])

cidade1 = int(input("RISUS:"))
cidade2 = int(input("boto fe:"))
a = 0
#dividindo por 111 vc vai ter sua posição de cada elemento por está razão dividimos por 111
while(cidade2!= -1):
	a+= b[cidade1//111-1,cidade2//111 -1]
	cidade1 = cidade2
	cidade2 = int(input("ESCREV DE NOVO:"))
print(a)