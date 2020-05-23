from numpy import*

v1 = array(eval(input("peso:")))
v2 = array(eval(input("altura:")))
vn = zeros(size(v1), dtype=float)

for e in range(size(v1)):
	imc = round((v1[e]/(v2[e]**2)),2)
	vn[e] = imc
print(vn)
print("O MAIOR IMC DA TURMA EH:",max(vn))
if(max(vn)<17):
	print("muito abaixo do peso".upper())
elif(max(vn)>17 and max(vn)<18.49):
	print("abaixo do peso".upper())
elif(max(vn)>18.5 and max(vn)<24.99):
	print("peso normal".upper())
elif(max(vn)>25 and max(vn)<29.99):
	print("acima do peso".upper())
elif(max(vn)>30 and max(vn)<34.99):
	print("obesidade".upper())
elif(max(vn)>35 and max(vn)<39.99):
	print("obesidade severa".upper())
elif(max(vn)>40):
	print("obesidade morbida".upper())

	
	
	
	