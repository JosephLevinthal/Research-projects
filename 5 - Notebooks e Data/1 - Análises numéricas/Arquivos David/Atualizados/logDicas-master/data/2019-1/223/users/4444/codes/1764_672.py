#from numpy  import *#
#a= array(eval(input('digite um numero intero: ')))#
						  
#a=ones(a, dtype=int)#
#print(a)#

from numpy import *
# Leitura dos vetores
notas = array(eval(input("Informe as notas: ")))
cred = array(eval(input("Informe os creditos: ")))
i = 0 # Variavel contadora
numerador = 0 # Acumula produto notas * creditos
denominador = 0 # Acumula os creditos
while (i < size(notas)):
	numerador = numerador + notas[i] * cred[i]
	denominador = denominador + cred[i]
	i = i + 1
coeficiente = numerador / denominador
print(round(coeficiente, 3))
						 
				  
				  