# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
cdx = float(input("Digite a coordenada x:"))
cdy = float(input("Digite a coordenada y:"))

if (2*cdx + cdy == 3):
	msg = "ponto pertence a reta"
else:
	msg = "ponto nao pertence a reta"

print(msg)	