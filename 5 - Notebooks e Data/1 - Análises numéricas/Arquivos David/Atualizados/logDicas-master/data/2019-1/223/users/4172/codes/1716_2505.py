from math import*

x= eval(input("angulo em radinas: "))
k= int(input("numero de k: "))

CO = 1     #contador

SINAL = -1 #o primeiro sinal

SOMA= x   #o primeiro termo

EXP=3      #o expoente

while(CO<k):
	SOMA= SOMA + (SINAL * ( (x)**EXP) / factorial(EXP ) )
	SINAL = SINAL * (-1)
	EXP = EXP + 2
	CO+=1
print(round(SOMA,10))