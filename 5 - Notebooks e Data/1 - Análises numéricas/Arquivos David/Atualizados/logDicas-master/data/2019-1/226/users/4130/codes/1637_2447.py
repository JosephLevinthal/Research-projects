n = float(input("valor do produto: "))
m = float(input("valor do pagamento: "))
			 
if(n > m):
	print("Falta", round(n - m, 2))
else:
	print("Troco de", round(m - n, 2))