a = float(input("Valor 'a' do intervalo fechado [a,b]: "))
b = float(input("Valor 'b' do intervalo fechado [a,b]: "))

c = float(input("Valor 'c' do intervalo fechado [c,d]: "))
d = float(input("Valor 'd' do intervalo fechado [c,d]: "))

print("Intervalo 1:", a, ",", b)
print("Intervalo 2:", c, ",", d)

if (a < b) and (c < d):
	if ((c >= a) and (c <= b)) or ((d >= a) and (d <= b)):
		print("Ha intersecao")
	else:
		print("Nao ha intersecao")
else:
	print("Entradas invalidas")

