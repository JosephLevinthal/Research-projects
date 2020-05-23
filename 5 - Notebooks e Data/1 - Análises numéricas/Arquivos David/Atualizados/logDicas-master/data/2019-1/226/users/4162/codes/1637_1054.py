# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x= float(input("insira a coordenada x: "))
y= float(input("insira a coordenada y: "))
r= 2*x+y

if r==3: 
	msg="ponto pertence a reta"
if r!=3:
	msg="ponto nao pertence a reta"

print(msg)






