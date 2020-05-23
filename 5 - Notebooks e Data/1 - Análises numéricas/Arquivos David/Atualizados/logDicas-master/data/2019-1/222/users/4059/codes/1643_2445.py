escala=input()
valor=int(input())

if (escala.upper()=='F'):
	print(round((5/9)*(valor-32),2))
else:
	print(round(((9/5)*valor + 32),2))