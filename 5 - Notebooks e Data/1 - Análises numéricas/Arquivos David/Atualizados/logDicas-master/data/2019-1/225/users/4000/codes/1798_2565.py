from numpy import*
m = array(eval(input("media final: ")))
pres = array(eval(input("presenca: ")))
ch = int(input("carga horaria: "))
ap = 0
rpn = 0
rpf = 0
for i in range(size(m)):
	if(m[i]>= 5 and pres[i]>=0.75*ch):
		ap = ap +1
	elif(m[i]<5):
		rpn = rpn + 1
	elif(pres[i]<0.75*ch):
		rpf = rpf + 1
v = zeros(3, dtype=int)
v[0]=ap
v[1]=rpn
v[2]=rpf
print(v)