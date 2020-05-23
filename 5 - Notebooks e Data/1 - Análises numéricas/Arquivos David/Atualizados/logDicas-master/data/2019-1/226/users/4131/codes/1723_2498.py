a = int(input("cidade a:"))
b = int(input("cidade b:"))
ca = float(input("crescimento a:"))
cb = float(input("crescimento b:"))

perca = ca / 100
percb = cb / 100
 
ano = 0

while (a<b):
	a = a + (a*perca)
	b = b + (b*percb)
	ano = ano + 1
print(ano)