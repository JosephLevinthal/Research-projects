from numpy import*
vet1=array(eval(input("digite a sequencia 1:")))
vet2=array(eval(input("digite a sequencia 2:")))
i=0
soma_vet1=0
soma_vet2=0
valor_vet1=0
valor_vet2=0
while(i<size(vet1)):
	if(vet1[i]==33 and vet2[i]==22):
		valor_vet1=1
		valor_vet2=0
	elif(vet1[i]==22 and vet2[i]==11):
		valor_vet1=1
		valor_vet2=0
	elif(vet1[i]==11 and vet2[i]==33):
		valor_vet1=1
		valor_vet2=0
	elif(vet1[i]==11 and vet2[i]==11):
		valor_vet1=0
		valor_vet2=0
	elif(vet1[i]==22 and vet2[i]==22):
		valor_vet1=0
		valor_vet2=0
	elif(vet1[i]==33 and vet2[i]==33):
		valor_vet1=0
		valor_vet2=0
	elif(vet1[i]==22 and vet2[i]==33):
		valor_vet2=1
		valor_vet1=0
	elif(vet1[i]==33 and vet2[i]==11):
		valor_vet2=1
		valor_vet1=0
	elif(vet1[i]==11 and vet2[i]==22):
		valor_vet2=1
		valor_vet1=0
	soma_vet1=soma_vet1+valor_vet1
	soma_vet2=soma_vet2+valor_vet2
	i=i+1
print(size(vet1))
if(soma_vet2==soma_vet1):
	print("EMPATE")
if(soma_vet2>soma_vet1):
	print("BARSANULFO")
if(soma_vet1>soma_vet2):
	print("EUSAPIA")
		

	
	
	
	
	
	
	
	
	
