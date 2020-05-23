valor = float(input("Digite um numero: "))
qticket = int(input("Digite um numero: "))
vticket = float(input("Digite um numero: "))
qonibus = int(input("Digite um numero: "))
vonibus = float(input("Digite um numero: "))

total=((qticket*vticket)+(qonibus*vonibus))
if(valor>=total):
	msg="suficiente".upper()
else:
	msg="insuficiente".upper()
	
print(msg)
