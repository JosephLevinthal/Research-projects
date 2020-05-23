# Teste seu codigo o final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import*
a = float ( input ( "Valor de a: " ) )
b = float ( input ( "Valor de b: " ) )
c = float ( input ( "Valor de c: " ) )

semiper = ( a + b + c ) / 2
Area = sqrt( semiper * (semiper - a) * (semiper - b) * (semiper - c) )
print ( round ( Area , 5 ))