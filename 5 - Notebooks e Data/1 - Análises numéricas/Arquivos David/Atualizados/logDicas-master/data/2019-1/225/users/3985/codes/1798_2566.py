from numpy import*

D = array(eval(input("Dias da semana: ")))

f1 = 0 #segunda
f2 = 0 #terça
f3 = 0 #quarta
f4 = 0 #quinta
f5 = 0 #sexta
f6 = 0 #sábado

for i in range(size(D)):
	if (D[i] == 2):
		f1 = f1 + 1
	elif (D[i] == 3):
		f2 = f2 + 1
	elif (D[i] == 4):
		f3 = f3 + 1
	elif (D[i] == 5):
		f4 = f4 + 1
	elif (D[i] == 6):
		f5 = f5 + 1
	elif (D[i] == 7):
		f6 = f6 + 1

F = f1 + f2 + f3 + f4 + f5 + f6
v = zeros(6, dtype=float)
for I in range(size(v)):
	v[0] = round(f1 * 100/F , 1)
	v[1] = round(f2 * 100/F , 1)
	v[2] = round(f3 * 100/F , 1)
	v[3] = round(f4 * 100/F , 1)
	v[4] = round(f5 * 100/F , 1)
	v[5] = round(f6 * 100/F , 1)
print(v)