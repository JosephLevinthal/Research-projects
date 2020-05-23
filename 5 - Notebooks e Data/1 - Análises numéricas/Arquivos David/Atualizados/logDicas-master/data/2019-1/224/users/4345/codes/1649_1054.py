# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
a= int(input("coordenada x:"))
b= int(input("coordenada y:"))
eq= (2*a + b)
if (eq==3):
   nsg= "ponto pertence n reta"
else:
	nsg="ponto nao pertence a reta"
	print(nsg)