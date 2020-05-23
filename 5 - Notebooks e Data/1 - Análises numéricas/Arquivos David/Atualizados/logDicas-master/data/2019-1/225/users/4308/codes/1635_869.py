# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
preco = float(input("Preco: "))
if (preco>=200) :
	desconto = preco - (preco * 0.05)
   print(float(desconto))
else :
   print(float(preco))