h = float(input("Altura da Torre da Lua: "))
qtd1 = float(input("Quantidade de metros que Equecrates sobe: "))
qtd2 = float(input("Quantidade de metos que Antistenes faz o guerreiro descer: "))
qtdAltura = qtd1
t = 1

while(qtdAltura <= h):
	qtdAltura = qtdAltura + qtd1
	if(qtdAltura < h):
		qtdAltura = qtdAltura - qtd2
	t = t + 1
	
print(t)