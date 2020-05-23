t=int(input("Quanto tempo em meses? "))
#Digitar as variaveis de entrada
Qf=1000000 + 42000
Q0=1500
Q=Qf/Q0

i=float(Q**(1/t))-1

if i <= 0.01:
 	imprima = "Real"

else:
	imprima = "Irreal"

print (i)
print (imprima)
