from numpy import*
p=array(eval(input("DIGITE O SEU PESO: ")))
a=array(eval(input("DIGITE A SUA ALTURA: ")))
v=zeros(size(a),dtype=float)
for i in range(size(p)):
	if(a[i]>0):
		v[i]=round(v[i]+(p[i]/a[i]**2), 2)
print(v)
print("O MAIOR IMC DA TURMA EH: ", max(v))
if(max(v)<17):
	print("MUITO ABAIXO DO PESO: ")
if(max(v)>=17) and (max(v)<=18.49):
	print("ABAIXO DO PESO")
if(max(v)>=18.5) and (max(v)<24.99):
	print("PESO NORMAL")
if(max(v)>=25) and (max(v)<29.99):
	print("ACIMA DO PESO")
if(max(v)>=30) and (max(v)<34.99):
	print("OBESIDADE")
if(max(v)>=35) and (max(v)<39.99):
	print("OBESIDADE SEVERA")
if(max(v)>40):
	print("OBESIDADE MORBIDA")