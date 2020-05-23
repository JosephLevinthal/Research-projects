# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

a = int( input ( "Valor de a: " ) )
b = int( input ( "Valor de b: " ) )
c = int( input ( "Valor de c: " ) )

print ( min (a , b, c ), a + b + c - min( a, b, c ) - max(a, b, c), max( a, b, c))