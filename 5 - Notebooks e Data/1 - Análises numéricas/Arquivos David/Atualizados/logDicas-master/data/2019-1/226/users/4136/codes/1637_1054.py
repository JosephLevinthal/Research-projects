# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
var1 = float(input("escreva as coordenadas de X: "))
var2 = float(input("escreva as coordenadas de Y: "))
formula = 2*var1 + var2 
if (formula == 3):
	mensagem = "ponto pertence a reta"
if (formula != 3):
	mensagem = "ponto nao pertence a reta"
print(mensagem)