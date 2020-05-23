from numpy import*
m = array(eval(input("medias: ")))
p = array(eval(input("presenca: ")))
h = float(input("carga horaria: "))
v = zeros(3, dtype=int)
ap = 0
rpn = 0 
rpf = 0
y = 0
for x in m:
	if (x>=5) and (p[y]>=h*0.75):
		ap+= 1
	elif (x<5) and (p[y]>h*0.75):
		rpn+= 1
	elif (p[y]<h*0.75):
		rpf+= 1
	y = y + 1
v[0] = ap
v[1] = rpn
v[2] = rpf
print(v)