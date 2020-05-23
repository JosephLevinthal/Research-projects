a=float(input("preco: "))
b=float(input("pagamento: "))
if (a>b):
	s=a-b
	print("Falta ", round(s,2))
else: 
	s=b-a
	print("Troco de", round(s,2))
	