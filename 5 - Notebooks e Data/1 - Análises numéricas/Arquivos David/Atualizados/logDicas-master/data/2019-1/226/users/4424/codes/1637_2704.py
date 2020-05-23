nota = float(input("nota: "))
b=input("vai receber bonificacao?") .upper()

if(b=="S"):
	
	total=nota + (nota*10/100)
else:
	total=nota
	

print(total)
