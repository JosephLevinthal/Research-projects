# Instituto de Computacao - UFAM
# Lab 04 - Ex 04
# 20 / 06 / 2016

qi = float(input("Quantia inicial: "))
tempo = int(input("Tempo de investimento: "))
juros = 4.0
t = 0
i=0
soma=qi


while (i<tempo):
	soma=soma+(juros/100)*soma
	i=i+1	

	print(round(soma,2))

	
