n = int(input("numero inteiro de 3 digitos: "))
dig1 = n // 100
dig23 = n - (dig1 *100)
k = n % dig23
if (k == 0):
	print("SIM")
else:
	print("NAO")