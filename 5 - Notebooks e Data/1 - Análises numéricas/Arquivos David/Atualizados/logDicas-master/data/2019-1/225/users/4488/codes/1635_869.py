# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
a= float(input("x="))
b= float(input("y="))

if(2*a+b==3):
	mensagem= "ponto pertence a reta"
else:
	mensagem= "ponto nao pertence a reta"
print(mensagem)