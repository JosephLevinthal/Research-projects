a = float(input("num. de habitates da cidade a: "))
b = float(input("num de habitantes da cidade b: "))
pa = float(input("percentual de a : "))
pb = float(input("percentual de b: "))


x = (pa/100)
y = (pb/100)

ano = 0 #contadora

while(a<b):
	a = a +(a *x)
	b = b + (b*y)
	ano = ano + 1
print(ano)
