from numpy import * 

a = array(eval(input("faltas: ")))
b = zeros(6,dtype=float)

for i in a:
	if i == 2:
		b[0] += 1
	elif i == 3:
		b[1] += 1
	elif i == 4:
		b[2] += 1
	elif i == 5:
		b[3] += 1
	elif i == 6:
		b[4] += 1
	elif i == 7:
		b[5] += 1
for i in range(size(b)):
	b[i] = round((b[i]*100)/size(a),1)
print(b)