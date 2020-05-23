inf = int(input("Digite: "))
cav = int(input("Digite: "))
pi = float(input("Digite: "))
pc = float(input("Digite: "))
soma = 0
mes = 0
while (inf + cav < 50000):
	inf = inf + (inf*pi)/100
	cav = cav + (cav*pc)/100
	soma = inf + cav
	mes = mes + 1
print(mes)
	
	