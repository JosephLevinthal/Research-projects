from numpy import * 
entrada = array(eval(input("digite os passageiros que entram: ")))
saida = array(eval(input("digite os passageiros que saem: ")))
i = 0
s = 0
while(i<size(entrada)):
	s = s + (entrada[i] - saida[i])
	i = i + 1
print(s)