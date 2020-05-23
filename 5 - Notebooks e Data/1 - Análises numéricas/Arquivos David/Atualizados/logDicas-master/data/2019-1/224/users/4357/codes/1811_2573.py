from numpy import*
p=array(eval(input("digite o numero:")))
h=array(eval(input("digite o numero:")))
d=zeros(size(p),dtype=float)
a=0
for i,j in zip(p,h):
	imc=i/j**2
	d[a]=round(imc,2)
	a=a+1
print(d)
print("O MAIOR B DA TURMA EH:",max(d))
if(max(d)<17):
	print("MUITO ABAIXO DO PESO")
elif(17<max(d)<18.49):
	print("ABAIXO DO PESO")
elif(18.5<max(d)<24.99):
	print("PESO NORMAL")
elif(25<max(d)<29.99):
	print("ACIMA DO PESO")
elif(30<max(d)<34.99):
	print("OBESIDADE")
elif(35<max(d)<39.99):
	print("OBESIDADE SEVERA")
else:
	print("OBESIDADE MORBIDA")