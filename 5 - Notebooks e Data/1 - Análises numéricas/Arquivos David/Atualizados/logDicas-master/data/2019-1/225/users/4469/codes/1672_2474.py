# Teste seu código com o dia do seu nascimento. Deu certo? E o dia de hoje?

# Que importante cientista nasceu em 4 de janeiro de 1643?
q = int(input())
mes = int(input())
ano = int(input())

m = mes
if(mes == 1 or mes == 2):
	m = mes + 12
	ano = ano - 1
k = ano % 100
j = ano / 100

h = (q + (13 * (m + 1) / 5) + k + (k / 4) + (j / 4) + 5 * j) % 7
if(h == 0):
	print("sabado")
elif(h == 1):
	print("domingo")
elif(h == 2):
	print("segunda")
elif(h == 3):
	print("terca")
elif(h == 4):
	print("quarta")
elif(h == 5):
	print("quinta")
elif(h == 6):
	print("sexta")