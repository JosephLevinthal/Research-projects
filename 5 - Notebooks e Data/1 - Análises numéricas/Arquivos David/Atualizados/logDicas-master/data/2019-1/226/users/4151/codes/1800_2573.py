from numpy import*
p=array(eval(input("peso: ")))
a=array(eval(input("altura: ")))
x=zeros(size(p))
for i in range(size(p)):
	x[i]=(round(p[i]/(a[i]*a[i]),2))
	
print(x)
print("O MAIOR IMC DA TURMA EH: ", max(x))
for i in range(size(x)):
	if(max(x)<17):
		mensagem=("MUITO ABAIXO DO PESO")
	elif(max(x)>17 and max(x)<18.49):
		mensagem=("ABAIXO DO PESO")
	elif(max(x)>18.5 and max(x)<24.99):
		mensagem=("PESO NORMAL")
	elif(max(x)>25 and max(x)<29.99):
		mensagem=("ACIMA DO PESO")
	elif(max(x)>30 and max(x)<34.99):
		mensagem=("OBESIDADE")
	elif(max(x)>35 and max(x)<39,99):
		mensagem=("OBESIDADE SEVERA")
	elif(max(x)>35 and max(x)<39,99):
		mensagem=("OBESIDADE MORBIDA")
print(mensagem)
	