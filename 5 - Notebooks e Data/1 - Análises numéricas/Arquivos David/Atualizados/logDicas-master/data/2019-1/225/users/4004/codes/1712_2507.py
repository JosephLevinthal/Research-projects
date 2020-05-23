q = int(input("quantidade de pirarucus iniciais: "))
p = float(input("porcentual de crescimento: "))

c = 0               #contador
f = q               #pirarucus
lim = 8000          #limite do tanque
p = p / 100         #porcentagem

while (f < lim) and (f > 0):
	c = c + 1
	v = int(input("vendas mensais: "))
	f = (f - v) + (f * p)
if f <= 0 :
	print("ZERO")
elif f >= lim:
	print("MAXIMO")
print(c)