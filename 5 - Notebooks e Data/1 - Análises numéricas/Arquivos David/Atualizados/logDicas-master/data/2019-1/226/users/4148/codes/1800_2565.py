from numpy import*

a = array(eval(input("media: ")))
b = array(eval(input("presenca: ")))
c = float(input("carga horaria: "))

cont = zeros(3, dtype=int)

for i in range(size(a)):
	
	if a[i] >= 5 and b[i] >= c * (75/100): #aprovados
		cont[0] = cont[0] + 1
		
	elif a[i] <=5 and b[i] >= c * (75/100):
		cont[1] = cont[1] +1
	
	elif a[i] >= 5 and b[i] <= c * (75/100):
		cont[2] = cont[2] + 1
		
print(cont)