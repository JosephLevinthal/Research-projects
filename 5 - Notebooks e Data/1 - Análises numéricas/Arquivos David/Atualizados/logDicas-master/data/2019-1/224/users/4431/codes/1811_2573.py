from numpy import*
x=array(eval(input("Digite as massas: ")))
y=array(eval(input("Digite as altuas: ")))
m=zeros(size(x),dtype(float))
h=0
for i in x:
	m[h]=m[h]+(i/(y[h]*y[h]))
	m[h]=round(m[h],2)
	h=h+1
print(m)
print("O MAIOR IMC DA TURMA EH:",max(m))

if(max(m)<17):
	print("MUITO ABAIXO DO PESO")
elif(max(m)>=17)and(max(m)<=18.49):
	print("ABAIXO DO PESO")
elif(max(m)>=18.5)and(max(m)<=24.99):
	print("PESO NORMAL")
elif(max(m)>=25)and(max(m)<=29.99):
	print("ACIMA DO PESO")
elif(max(m)>=30)and(max(m)<=34.99):
	print("OBESIDADE")
elif(max(m)>=35)and(max(m)<=39.99):
	print("OBESIDADE SEVERA")
elif(max(m)>=40):
	print("OBESIDADE MORBIDA")
	