# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("Digite um numero:"))
y = float(input("Digite um numero:"))
if (2*x + y - 3 == 0): 
	msg = "ponto pertence a reta"
else:
	msg = "ponto nao pertence a reta"
print(msg)