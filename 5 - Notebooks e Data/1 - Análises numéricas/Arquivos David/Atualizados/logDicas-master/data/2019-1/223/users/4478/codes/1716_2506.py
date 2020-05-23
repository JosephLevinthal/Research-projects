a = int(input("qtde inicial: "))
b = int(input("percentual de crescimento: "))/100
c = int(input("venda anual: "))

anos = 0


while(a > 0  and a < 12000):
	a = a+(a * b)-c
	anos = anos + 1
	if(a < 0):
		
		mensagem = "EXTINCAO"
	else:
		mensagem = "LIMITE"
print(mensagem)
print(anos)
