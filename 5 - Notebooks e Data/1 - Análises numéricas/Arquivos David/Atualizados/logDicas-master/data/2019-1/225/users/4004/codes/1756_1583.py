from numpy import*

x = str(input("string: "))

s = len(x)/3     #tamaho e limite
i = 0            #indice
y = 0            #string imagem
t = 2

while i > s:
	if (x[t:] == x[-3:]) or (x[0:] == x[-3]):
		i = i + 1
		y = y + x[i]
print(y)