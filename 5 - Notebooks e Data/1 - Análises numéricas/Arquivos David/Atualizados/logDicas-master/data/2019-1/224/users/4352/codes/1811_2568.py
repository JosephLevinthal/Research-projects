from numpy import*
a = int(input("digite o numero de arteriscos: "))
for i in range(a):
	ch = "*"*(a-i) + "o"*(i*2) + "*"*(a-i)
print(ch)