a = int(input("cidade a:"))
b = int(input("cdade b:"))
pa = float(input("percentual a:"))
pb = float(input("percentual b:"))
percA = pa/100
percB = pb/100
ano = 0
while(a < b):
	a = a+(a*percA)
	b = b+(b*percB)
	ano = ano + 1
print(ano)