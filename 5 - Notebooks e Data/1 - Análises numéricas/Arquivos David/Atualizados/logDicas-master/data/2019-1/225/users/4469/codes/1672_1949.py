x = int(input())
y = int(input())

x1 = x // 10
x2 = x % 10

y1 = y // 10
y2 = y % 10

if(x1 == y1 and x2 == y2):
	print("Ganhou R$ 100.000,00")
elif(x1 == y2 and x2 == y1):
	print("Ganhou R$ 50.000,00")
elif(x1 == y1 or x2 == y2 or x1 == y2 or x2 == y1):
	print("Ganhou R$ 1.000,00")
else:
	print("Perdeu")