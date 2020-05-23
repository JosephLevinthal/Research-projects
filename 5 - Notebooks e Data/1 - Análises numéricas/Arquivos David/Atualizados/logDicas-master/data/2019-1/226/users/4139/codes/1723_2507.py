qi = int(input("quantidade inicial de pirarucus:"))
pc = int(input("percentual de crescimento: "))


p = pc /100

mes = 0

while(qi > 0 and qi < 8000):
	qv = int(input("quantidade de peixes vendidos: "))
	qi += (qi*p)-qv
	mes = mes + 1

if(qi<= 0):
	print("ZERO")
else:
	print("MAXIMO")
print(mes)