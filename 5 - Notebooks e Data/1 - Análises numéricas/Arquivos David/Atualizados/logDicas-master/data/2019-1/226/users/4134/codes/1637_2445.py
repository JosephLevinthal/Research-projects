esc = input("Qual escala? (C/F) ")
tmp = int(input("Temperatura proposta: "))

if (esc.upper() == "c"): 
	msg = tmp*(5/9) + 32
else:
	msg = (tmp - 32)*(5/9)
	
print(msg)
