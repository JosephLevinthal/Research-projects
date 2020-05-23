from numpy import *
medias=array(eval(input("digite o vetor :")))
while(size(medias)>1):
	soma=0
	for pos in medias:
		if(5<= pos <7):
			soma=soma+1
	print(soma)
	medias=array(eval(input("digite a media:")))
		