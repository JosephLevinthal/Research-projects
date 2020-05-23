from numpy import*
a = array(eval(input("numero de alunos: ")))
p=0
for i in a:
	if(i % 5 == 0):
		p= p + 1
print(p)
impar = zeros(p, dtype = int)
b = 0
for i in range (size(a)):
	if(a[i] % 5 == 0):
		impar[b] = i
		b = b + 1
print(impar)

	
	
