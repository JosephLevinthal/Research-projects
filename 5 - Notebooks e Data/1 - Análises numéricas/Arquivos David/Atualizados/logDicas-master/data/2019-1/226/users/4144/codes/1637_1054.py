# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("digite a coordenada x: "))
y = float(input("digite a coordenada y: "))
if ((2 * x) + y == 3):
	men = "ponto pertence a reta"
else:
	men = "ponto nao pertence a reta"
print(men)
