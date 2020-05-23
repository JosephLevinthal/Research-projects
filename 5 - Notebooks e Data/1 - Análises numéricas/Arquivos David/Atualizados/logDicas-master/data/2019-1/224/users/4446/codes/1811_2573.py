from numpy import *
p=array(eval(input("digite o peso: ")))
a=array(eval(input("digite a altura: ")))
x=size(p)
z=zeros(x, dtype=float)

for i in range(size(p)):
	imc=p[i]/(a[i]*a[i])
	z[i]=round(imc, 2)
print(z)
print("O MAIOR IMC DA TURMA EH:",round(max(z), 2))
w=round(max(z), 2)
if (w<17):
	print("muito abaixo do peso".upper())
if(w>=17 and w<=18.49):
	print("abaixo do peso".upper())
if(w>=18.5 and w<=24.99):
	print("peso normal".upper())
if(w>=25 and w<=29.99):
	print("acima do peso".upper())
if(w>=30 and w<=34.99):
	print("obesidade".upper())
if(w>=35 and w<=39.99):
	print("obesidade severa".upper())
if(w>40):
	print("obesidade morbida".upper())