# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x= float(input("qual a coordenada x? "))
y= float(input("qual a coordenada y? "))

soma= 2*x+y
if (soma==3):
	msg= "ponto pertence a reta"
else:
	msg= "ponto nao pertence a reta"
print(msg)