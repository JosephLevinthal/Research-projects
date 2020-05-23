from numpy import*
p = array(eval(input("massa:")))
a = array(eval(input("altura:")))
n = size(p)
b = zeros(n)
i = 0 
for x in p:
	b[i] = round((x/a[i]**2),2)
	i = i + 1
print(b)
print("O MAIOR IMC DA TURMA EH:",max(b))
if(max(b)<17):
	print("MUITO ABAIXO DO PESO")
elif(17 <= max(b)<=18.49):
	print("ABAIXO DO PESO")
elif(18.5<= max(b)<=24.99):
	print("PESO NORMAL")
elif(25<= max(b)<=29.99):
	print("ACIMA DO PESO")
elif(30<= max(b)<=34.99):
	print("OBESIDADE")
elif(35<= max(b)<=39.99):
	print("OBESIDADE SEVERA")
elif( max(b)>= 40):
	print("OBESIDADE MORBIDA")

		
		
		
		
		
		
	
	
	
	
	
	