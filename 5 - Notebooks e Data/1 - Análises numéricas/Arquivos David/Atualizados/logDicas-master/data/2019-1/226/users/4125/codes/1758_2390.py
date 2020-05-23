from numpy import*
n = array(eval(input("digite os presentes por mes: ")))
n1 = array(eval(input("digite os ausentes por mes: ")))

a = max(n)
i = 0
mes = 1
while(n[i]!=max(n)):
	mes = mes + 1
	i = i + 1
print(mes)