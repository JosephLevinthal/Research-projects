# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
entrada=int(input("numero de quatro digitos"))
primeiro_digito= entrada//1000
segundo_digito=entrada%1000//100
terceiro_digito=entrada%100//10
quarto_digito=entrada%100%10
print(primeiro_digito+segundo_digito+terceiro_digito+quarto_digito)