var1=float(input("horas extras:"))
var2=float(input("horas faltosas:"))
print(var1, "extras e",var2, "de falta")

H=((var1)-(1/4*var2))	
if(H>400):
	print("R$ 500.0")
elif((H>0) and (H<=400)):
	print("R$ 100.0")	
	
	