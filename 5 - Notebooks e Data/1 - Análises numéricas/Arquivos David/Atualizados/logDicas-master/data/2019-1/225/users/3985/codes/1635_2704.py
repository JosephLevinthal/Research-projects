x= float(input("Nota do aluno:"))
v= input("S / N?")

if (v.upper()== "S"):
	k= x+(x/100*10)
else:
	k= x
print(float(k))