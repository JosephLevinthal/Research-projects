# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x=int(input("escolhaum numero: "))
y=int(input("escolhaum numero: "))
p=(x,y)
r=2*x+y-3
if(r==0):
	mensagem="ponto pertence a reta"
else:
	mensagem="ponto nao pertence a reta"
print(mensagem)