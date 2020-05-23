n = int(input("Insira o numero n: "))

N = n - (n // 100) * 100

if(n % N == 0):
	mensagem = "SIM"
else:
	mensagem = "NAO"
	
print(mensagem)