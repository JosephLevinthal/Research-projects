# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

x= float(input("Insira o ponto x:"))
y= float(input("Insira o ponto y:"))

p= 2*x+y
if (p==3):
	msg= "ponto pertence a reta"
else:
	msg= "ponto nao pertence a reta"
print(msg.lower())