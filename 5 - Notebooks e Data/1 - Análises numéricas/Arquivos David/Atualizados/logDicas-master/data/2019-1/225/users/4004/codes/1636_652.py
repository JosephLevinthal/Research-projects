n = int(input("um numero entre 100 e 999: "))

if 100 <= n <= 999:
	right_n = (n // 100)
	exclusao_n = right_n * 100
	nfe = n - exclusao_n
	if n % nfe == 0:
		print("SIM")
	else:
		print("NAO")