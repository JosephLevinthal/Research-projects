idade=int(input("qual a idade?: "))
if(idade<18):
   mensagem="nao_eleitor"
else:
   mensagem="eleitor"
print(mensagem.lower())