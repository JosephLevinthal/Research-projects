n = int(input("insira o numero n:"))

N = n - (n//100) *100 
if (n % N == 0):
	mensagem = print("SIM")
else:
	mensagem = print("NAO")