valor = float(input("Quanto tem? "))
ru = int(input("Quantos tickets? "))
vru = float(input("Valor do ticket: "))
passes = int(input("Quantos passes: "))
vpasses = float(input("Valor dos passes: "))

if(valor >= ru * vru + passes * vpasses):
	mensagem = "suficiente"

else:
	mensagem = "insuficiente"
	
print(mensagem.upper())