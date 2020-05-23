f = int(input("digite a qty de seguidores de forseti: "))
l = int(input("digite a qty de seguidores de loki: "))
a = float(input("digite o percentual de crescimento do deus forseti: "))
b = float(input("digite o percentual de crescimento do deus loki: "))

a = a/100
b = b/100


h = 0

while f > l:
	x = f*a
	f = x+f
	y = l*b
	l = y+l
	h += 1
print(h)