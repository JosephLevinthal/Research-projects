from numpy import*
x = int(input("indice: "))
y = arange(x)
z = zeros(x * 2, dtype=int)

j = 0
i = -1

for i in range(x,0,-1):
	print(i * "*")
for i in range(1,x + 1):
	print(i * "*")