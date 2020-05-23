senha =int(input("Informe a senha :"))
primeira =  senha // 100000 % 10
segunda  =  senha // 10000 % 10
terceira =  senha // 1000 % 10
quarta   =  senha // 100 % 10
quinta   =  senha // 10 % 10
sexta    =  senha // 1 % 10
parte1 = segunda+quarta+sexta
parte2 = primeira+terceira+quinta

if((parte1 % parte2)==0):
  mensagem=("acesso liberado") 
else:	
  mensagem=("senha invalida")

print(mensagem)
