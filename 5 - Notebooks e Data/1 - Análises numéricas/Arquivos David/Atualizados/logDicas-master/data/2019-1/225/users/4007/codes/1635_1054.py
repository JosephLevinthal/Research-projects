# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("digite o valor de x: "))
y = float(input("digite o valor de y: "))
reta = (2*x) + y
if (reta == 3):
	msg = "ponto pertence a reta"
else:
	msg = "ponto nao pertence a reta"
	
print(msg.lower())