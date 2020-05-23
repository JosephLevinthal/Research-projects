from numpy import*
p = array(eval(input("peso: ")))
a = array(eval(input("altura:")))

v=zeros(size(p),dtype=float)
h=0
for i in range(size(p)):
	IMC=round((p[i]/(a[i]**2)),2)
	v[i]=IMC
	h+=1
print(v)
print("O MAIOR IMC DA TURMA EH:", max(v))
if(max(v)<17):
	print("muito abaixo do peso".upper())
elif(max(v)>17 and max(v)<18.49):
	print("abaixo do peso".upper())
elif(max(v)>18.5 and max(v)<24.99):	
	print("peso normal".upper())
elif(max(v)>25 and max(v)<29.99):	
	print("acima do peso".upper())
elif(max(v)>30 and max(v)<34.99):
	print("obesidade".upper())
elif(max(v)>35 and max(v)<39.99):
	print("obesidade severa".upper())
elif(max(v)>40):
	print("obesidade morbida".upper())
	
	