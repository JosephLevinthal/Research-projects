from numpy import*
n = array(eval(input("Vetor: ")))
i = 0 #contadora
v = 0 #acumuladora
h = 0
while (i < size(n)):
	h = h + log(n[i] + 1) 
	i = i + 1
m = exp(h / size(n)) - 1
print(round(m, 2))
	