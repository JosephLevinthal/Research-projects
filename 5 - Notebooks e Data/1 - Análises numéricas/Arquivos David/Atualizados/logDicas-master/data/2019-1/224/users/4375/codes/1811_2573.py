from numpy import*
p=array(eval(input("peso dos alunos: ")))
a=array(eval(input("altura dos alunos: ")))
x=zeros(size(a), dtype=float)
for i in range (size(p)):
	if(a[i]>0):
		x[i]=round(x[i]+(p[i]/(a[i]**2)),2)
print(x)
print("O MAIOR IMC DA TURMA EH:", max(x))
if(max(x)<17):
	print("MUITO ABAIXO DO PESO")
if(max(x)>=17) and (max(x)<=18.49):
	print("ABAIXO DO PESO ")
if(max(x)>=18.5) and (max(x)<24.99):
	print("PESO NORMAL")
if(max(x)>=25) and (max(x)<29.99):
	print("ACIMA DO PESO")
if(max(x)>=30) and (max(x)<34.99):
	print("OBESIDADE")
if(max(x)>=35) and (max(x)<39.99):
	print("OBESIDADE SEVERA")
if(max(x)>=40):
	print("OBESIDADE MORBIDA")


