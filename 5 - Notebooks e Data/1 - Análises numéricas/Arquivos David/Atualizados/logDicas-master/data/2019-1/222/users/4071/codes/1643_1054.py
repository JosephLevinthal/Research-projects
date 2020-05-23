# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
corA= int(input("leia a coordenada X:"))
corB= int(input("leia a coordenada Y:"))
if (2*corA+corB==3):
	mensagem= "ponto pertence a reta"
else:
	mensagem="ponto nao pertence a reta"
print(mensagem)