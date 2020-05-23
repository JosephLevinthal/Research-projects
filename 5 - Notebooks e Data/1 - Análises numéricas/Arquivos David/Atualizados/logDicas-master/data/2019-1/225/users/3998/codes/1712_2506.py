qi= int(input("quantidade inicial: "))
qc= float(input("percentual de crescimento: "))
qv= int(input("quantidade pra venda: "))

a = 0

while(qi < 12000) and (qi > 0):
	qi = qi +((qi * qc /100)) -qv
	a = a + 1

if(qi >= 12000):
	print("LIMITE")
elif(qi <= 0):
	print("EXTINCAO")
print(a)