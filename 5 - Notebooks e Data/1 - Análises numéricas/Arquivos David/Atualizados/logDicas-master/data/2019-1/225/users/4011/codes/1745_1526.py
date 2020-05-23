qt = int(input("Quantidade inicial de mana da bruxa: "))
gd = int(input("Quantidade do gasto diario: "))
qr = int(input("Quantidade da recuperacao por noite: "))

mana = qt
dias = 0

while( mana > 0):
	
	mana = mana - gd + qr
	dias = dias + 1
	
print( dias )