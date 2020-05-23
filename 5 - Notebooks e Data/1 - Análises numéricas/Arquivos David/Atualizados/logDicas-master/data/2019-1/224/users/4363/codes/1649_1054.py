# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
a = float(input("coordenada x:"))
b = float(input("coordenada y:"))
if (2*a+b==3):
	msg= " ponto pertence a reta"
else:
	msg= "ponto nao pertence a reta"
print(msg)