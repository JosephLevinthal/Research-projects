var1=float(input("preco:"))
var2=float(input("pagamento:"))
x=float(var1-var2)
y=float(var2-var1)
if(var1 > var2):
	mensagem="Falta "
	print(mensagem+x)
else:
	mensagem=  "Troco de "
	print(mensagem+y)