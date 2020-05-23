ano = 0

ha = int(input("insira a entrada:"))
hb = int(input("insira a entrada:"))
a = float(input("insira o percentual de crescimento da cidade a:"))
b = float(input("insira o percentual de crescimento da cidade b:"))


while(ha < hb):
	ca = (ha * a)/100
	cb = (hb * b)/100
	ha = ha + ca
	hb = hb + cb
	ano = ano + 1
print(ano)
