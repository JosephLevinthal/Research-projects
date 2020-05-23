senha = int(input("Senha: "))

numerador = 0
denominador = 0

if(len(str(senha)) % 2 == 0):
	contador = 0 # Se contador for par, entao eh a vez de somar o digito ao numerador
else:
	contador = 1 # Se contador for impar, entao eh a vez de somar o digito ao denominador

while(senha > 0):
	if(contador % 2 == 0):
		numerador = numerador + (senha % 10)
	else:
		denominador = denominador + (senha % 10)
		
	senha = senha // 10
	contador = contador + 1
	
if((numerador % denominador == 0) or (denominador % numerador == 0)):
	print("acesso liberado")
else:
	print("senha invalida")