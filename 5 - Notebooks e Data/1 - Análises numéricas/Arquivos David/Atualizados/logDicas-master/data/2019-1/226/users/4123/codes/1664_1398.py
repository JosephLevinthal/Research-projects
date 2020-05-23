tmp = float(input())
if tmp > 200:
	valor = 8000 + 100*200 + (tmp-200)*90
	print(round(valor,2))
else:
	print(round(5000+tmp*100,2))