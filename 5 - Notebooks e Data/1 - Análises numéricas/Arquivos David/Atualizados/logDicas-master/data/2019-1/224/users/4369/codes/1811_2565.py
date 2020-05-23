from numpy import*
mf = array(eval(input("Digite a media final: ")))
hf = array(eval(input("Digite o n de horas em sala de aula dos alunos: ")))
f = float(input("Digite o numero de horas: "))
v = zeros(3, dtype = int)
r = f * 75 / 100 
for i in range(size(mf)):
	if mf[i] >= 5 and f[i] >= r:
		v[0] = v[0] + 1
	if mf[i] < 5:
		v[1] = v[1] + 1
	if f[i] < r:
		v[2] = v[2] + 1
print(v)
