from numpy import*

v = array(eval(input("Jogadas de Eusapia: ")))
b = array(eval(input("Jogadas de Barsanulfo: ")))

p=0
ve=0
vb=0

while(p < size(v) and p < size(b)):
	vj = v[p]
	bj = b[p]
	p = p + 1

	if (vj == 11 and bj == 33):
		ve = ve + 1
	if (vj == 11 and bj == 22):
		vb = vb + 1
	if (vj == 22 and bj == 11):
		ve = ve + 1
	if (vj == 22 and bj == 33):
		vb = vb + 1
	if (vj == 33 and bj == 11):
		vb = vb + 1
	if (vj == 33 and bj == 22):
		ve = ve + 1

print(size(v))
if (vb < ve):
	print("EUSAPIA")
elif (vb > ve):
	print("BARSANULFO")
elif (vb == ve):
	print ("EMPATE")