senha = int(input("digite a senha: "))
dig1 = senha // 100000
dig2 = (senha % 100000) // 10000
dig3 = (senha % 10000) // 1000
dig4 = (senha % 1000) // 100
dig5 = (senha % 100) // 10
dig6 = senha % 10

if (((dig2 + dig4 + dig6) % (dig1 + dig3 + dig5)) == 0):
	print("acesso liberado")

else:
	print("senha invalida")
	
 