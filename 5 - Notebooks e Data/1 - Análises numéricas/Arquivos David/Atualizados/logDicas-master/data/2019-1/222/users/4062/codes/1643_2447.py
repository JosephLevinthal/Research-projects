a= float(input("qual o preco? "))
b= float(input("qual o pagamento ? "))
ft= round(a-b,2) 
tf= round(b-a,2)
if(a>b):
	print("Falta", ft)
else:
	print("Troco de", tf)
