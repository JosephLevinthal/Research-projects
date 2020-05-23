from numpy import*
vm = array(eval(input("vetor de medias:")))
vf = array(eval(input("vetor de frequencia:")))
c = int(input("carga horaria:"))

v = zeros(3 , dtype=int)

ap = 0
rn = 0
rf = 0
f = c * 75/100
for i in range(size(vm)):
	if(vm[i] >= 5 and vm[i] <= 10 and vf[i] >= f):
		ap = ap + 1
	elif(vm[i] < 5):
		rn = rn + 1
	elif(vf[i] < f):
		rf = rf + 1
v[0] = ap
v[1] = rn
v[2] = rf
print(v)