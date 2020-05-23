# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("x: "))
y = float(input("y: "))
#m = (2 * x + y - 3 == 0)
if (2 * x + y - 3 == 0):
	resultado = "ponto pertence a reta"
else: 
	resultado = "ponto nao pertence a reta"
print(resultado)