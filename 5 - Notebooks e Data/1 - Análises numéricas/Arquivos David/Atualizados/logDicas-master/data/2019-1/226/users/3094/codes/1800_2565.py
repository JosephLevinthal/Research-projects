from numpy import *

mf = array(eval(input("media final: ")))
f = array(eval(input("frequencia: ")))
ch = int(input("carga horaria: "))

cont = zeros(3, dtype=int)

for i in range(size(mf)):
	if mf[i] >= 5 and f[i] >= ch * (75/100):
		cont[0] = cont[0] + 1
	elif mf[i] < 5 and f[i] >= ch * (75/100):
		cont[1] = cont[1] + 1
	elif mf[i] >= 5 and f[i] < ch * (75/100):
		cont[2] = cont[2] + 1
print(cont)