# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
preco_i = float(input("preco inicial: "))
desconto = preco_i * 5 /100
preco_final = preco_i - desconto
print(round(preco_final, 2))