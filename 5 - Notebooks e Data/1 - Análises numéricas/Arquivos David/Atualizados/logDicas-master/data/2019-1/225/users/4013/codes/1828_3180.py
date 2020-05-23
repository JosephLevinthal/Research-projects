from numpy import*
vet = array(eval(input("sorotipos:")))
f = zeros(4 , dtype=int)
a = 0
b = 0
c = 0
d = 0
for i in range(size(vet)):
	if(vet[i] == 1):
		a = a+1
	elif(vet[i] == 2):
		b = b+1
	elif(vet[i] == 3):
		c = c+1
	elif(vet[i] == 4):
		d = d+1
f[0]=a
f[1]=b
f[2]=c
f[3]=d
print(f)