senha = int(input("senha: "))
resto = senha % 10
dig6 = resto
senha = (senha - resto) // 10

resto = senha % 10
dig5 = resto
senha = (senha - resto) // 10

resto = senha % 10
dig4 = resto
senha = (senha - resto) // 10

resto = senha % 10
dig3 = resto
senha = (senha - resto) // 10

resto = senha % 10
dig2 = resto
senha = (senha - resto) // 10

resto = senha % 10
dig1 = resto
senha = (senha - resto) // 10

soma1 = dig2 + dig4 + dig6
soma2 = dig1 + dig3 + dig5
rm = soma1 % soma2

if (rm == 0):
	print('acesso liberado')
	
else:
	print('senha invalida')