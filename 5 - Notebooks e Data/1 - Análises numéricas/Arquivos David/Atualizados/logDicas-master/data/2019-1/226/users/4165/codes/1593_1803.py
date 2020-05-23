num = int(input( "qual o seu numero"))
a = num//1000 * 2
b = num//100 * 3
c = num//10 * 4
d = num//1 * 5
soma = ( a + b + c + d )
divisaor = ( soma % 11 )
print( soma )