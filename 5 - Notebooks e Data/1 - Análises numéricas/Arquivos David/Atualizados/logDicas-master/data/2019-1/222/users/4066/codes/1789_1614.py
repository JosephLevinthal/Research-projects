from numpy import *
n = array(eval(input("Nome dos alimentos: ")))
q = array(eval(input("Quantidade: ")), dtype=float)

t = 0

qt = 0
i = 0

while (t < size(q)):
	if (n[t] == "BANANA"):
		q[t] = q[t]*(0.97)
	elif (n[t] == "BIFE"):
		q[t] = q[t]*(2.95)
	elif (n[t] == "FEIJOADA"):
		q[t] = q[t]*(1.27)
	elif (n[t] == "OMELETE"):
		q[t] = q[t]*(1.04)
	elif (n[t] == "TOMATE"):
		q[t] = q[t]*(0.2)

	t = t + 1
	
while (i < size(q)):
	qt = qt + q[i]
	i = i + 1
	
print(qt)


