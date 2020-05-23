# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrig
x=int(input("qual o valor de x? "))
y=int(input("qual o valor de y? "))
reta=2*x+y
if(reta==3):
	mensagem=("ponto pertence a reta ")
else:
	mensagem=("ponto nao pertence a reta ")
print(mensagem.lower())



