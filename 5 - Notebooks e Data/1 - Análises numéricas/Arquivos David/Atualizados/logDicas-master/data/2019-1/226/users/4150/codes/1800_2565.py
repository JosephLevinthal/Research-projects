from numpy import*

m = array(eval(input("digite: ")))
p = array(eval(input("digite: ")))
c = int(input("carga horaria: "))

x = zeros (3, dtype = int)

for i in range(size(m)):
	if m[i] >= 5 and (p[i]*100/c) >= 75:
		x[0] = x[0] + 1
	elif m[i] < 5 and (p[i]*100/c) >= 75:
		x[1] = x[1] + 1
	elif m[i] >=5 and (p[i]*100/c) < 75:
		x[2] = x[2] + 1
print(x)
		
		