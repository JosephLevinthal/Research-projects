from numpy import *
M=array(eval(input("digite as medias: ")))
while(size(M)>1):
	soma=0
	for pos in M:
		if(5<= pos < 7):
			soma = soma + 1
	print(soma)
	M=array(eval(input("digite outas medidas: ")))