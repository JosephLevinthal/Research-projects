# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
v= float(input("velocidade inicial:"))
a= radians(float(input("angulo:")))
d= float(input("distancia:"))
r=((v**2)*sin(2*a))/9.8

p= d - r

if(abs(p)<0.1):
	mensagem = "sim"
else:
	mensagem = "nao"
print(mensagem)