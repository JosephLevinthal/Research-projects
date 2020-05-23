x = int(input("qtde inicial: "))
bc = int(input("baloes construidos: "))
bd = int(input("baloes destruidos: "))
semana = 0
frota = x
while(frota >= 0 and frota <= 200):
	frota = frota + bc
	total = frota - bd
	semana = semana + 1
print(semana)