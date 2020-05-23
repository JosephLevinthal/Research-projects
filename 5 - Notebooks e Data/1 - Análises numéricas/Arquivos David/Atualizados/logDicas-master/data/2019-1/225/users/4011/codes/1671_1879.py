# Ao testar sua solução, não se limite ao caso de exemplo.

s = float(input("Coloque o numero de horas extras que o funcionario trabalhou: "))
f = float(input("Coloque o numero de horas que o funcionario nao trabalhou: "))

print( s ,"extras e" , f , "de falta" )

h = (s) - (0.25 * f)

if ( h > 400 ):
	print( "R$", 500.0 )
else:
	print( "R$", 100.0 )
