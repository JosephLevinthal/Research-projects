senha = int(input("senha: ")) # Max ta de sacanagem
if(senha < 10) :
	d1 = 0
	d2 = 0
	d3 = 0
	d4 = 0
	d5 = 0
	d6 = senha
	if(senha == 0) :
		print("acesso liberado")
	else :
		print("senha invalida")
if(10 <= senha <100) :
	d1 = 0
	d2 = 0
	d3 = 0
	d4 = 0
	d5 = senha // 10
	d6 = senha % 10
	if(d1 + d3 + d6 == 0) :
		print("senha invalida")
	else :	
		if((d2 + d4 + d6) % (d1 + d3 + d5) == 0) :
			print("acesso liberado")
		else :
			print("senha invalida")
if(100 <= senha < 1000) :
	d1 = 0
	d2 = 0
	d3 = 0
	d4 = senha // 100
	d5 = (senha % 100) // 10
	d6 = (senha % 100) % 10
	if(d1 + d3 + d6 == 0) :
		print("senha invalida")
	else :	
		if((d2 + d4 + d6) % (d1 + d3 + d5) == 0) :
			print("acesso liberado")
		else :
			print("senha invalida")
if(1000 <= senha < 10000) :
	d1 = 0
	d2 = 0
	d3 = senha // 1000
	d4 = (senha % 1000) // 100
	d5 = ((senha % 1000) % 100) // 10
	d6 = ((senha % 1000) % 100) // 100
	if(d1 + d3 + d6 == 0) :
		print("senha invalida")
	else :	
		if((d2 + d4 + d6) % (d1 + d3 + d5) == 0) :
			print("acesso liberado")
		else :
			print("senha invalida")
if(10000 <= senha < 100000) :
	d1 = 0
	d2 = senha // 10000
	d3 = (senha % 10000) // 1000
	d4 = ((senha % 10000) % 1000) // 100
	d5 = (((senha % 10000)% 1000)% 100) // 10
	d6 = (((senha % 10000)% 1000)% 100) % 10
	if(d1 + d3 + d6 == 0) :
		print("senha invalida")
	else :	
		if((d2 + d4 + d6) % (d1 + d3 + d5) == 0) :
			print("acesso liberado")
		else :
			print("senha invalida")
if(100000 <= senha < 1000000) :
	d1 = senha // 100000
	d2 = (senha % 100000) // 10000
	d3 = ((senha % 100000) % 10000) // 1000
	d4 = (((senha % 100000) % 10000) % 1000) // 100
	d5 = ((((senha % 100000) % 10000) % 1000) % 100) // 10
	d6 = ((((senha % 100000) % 10000) % 1000) %100) %  10

	else :	
		if((d2 + d4 + d6) % (d1 + d3 + d5) == 0) :
			print("acesso liberado")
		else :
			print("senha invalida") 	

	
	