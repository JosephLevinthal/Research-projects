from numpy import*

vet1 = array(eval(input("Digite os gols: ")))
vet2 = array(eval(input("Digite os gols: ")))
vt1 = 0
vp1 = 0
vd1 = 0
a = zeros(3, dtype=int)

for i in range(size(vet1)):
		
	if	( vet1[i] > vet2[i]):
			vt1 = vt1 + 1
	elif	( vet1[i] == vet2[i]):
				vp1 = vp1 + 1
	elif	(  vet1[i] < vet2[i]):
				vd1 = vd1 + 1
	a[0] = vt1
	a[1] = vp1
	a[2] = vd1
print(a)

	