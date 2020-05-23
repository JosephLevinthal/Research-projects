he= float(input("he:"))
hf= float(input("hf:"))
h= (he-(1/4*hf))
print(he, "extras e",hf,"de falta")
if(h> 400):
	mensagem= 500.00
	print("R$", round(mensagem, 2))
else:
	mensagem= 100.00
	print("R$", round(mensagem, 2))
	