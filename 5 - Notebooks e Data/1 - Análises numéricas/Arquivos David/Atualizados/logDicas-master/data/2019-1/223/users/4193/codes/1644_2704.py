# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
nota=float(input("qual foi a nota ?:"))
bonificacao=input("vai receber  bonificacao?:")
if (bonificacao=="S"):
   mensagem=nota+(nota*0.1)
else:
   mensagem=nota
print(round(mensagem , 2))
