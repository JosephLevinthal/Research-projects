from numpy import*
p = array(eval(input("Massa: ")))
h = array(eval(input("Altura: ")))
IMC = zeros(size(p))
for i in range(size(p)):
	IMC[i] = round((p[i]/h[i]**2),2)
print(IMC)	
x= "O MAIOR IMC DA TURMA EH:"
print(x,max(IMC))
y=max(IMC)
if(y<17):
	print("MUITO ABAIXO DO PESO")
elif(y>=17 and y<18.49):
	print("ABAIXO DO PESO")
elif(y>=18.5 and y<=24.99):
	print("PESO NORMAL")
elif (y>=25 and y<=29.99):
	print("ACIMA DO PESO")
elif(y>=30 and y<=34.99):
	print("OBESIDADE")
elif(y>=35 and y<=39.99):
	print("OBESIDADE SEVERA")
elif(y>=40):
	print("OBESIDADE MORBIDA")




