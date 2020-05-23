p = int(input("insira a quantidade inicial de pirarucus:"))
pc = float(input("insira o percentual de crescimento dos pirarucus:"))
qm = int(input("insira a quantidade de pirarucus retirados cada mes:"))

mes = 0

while(p > 0 and p < 8000):
	cp = (p * pc)/100
	p = p + cp - qm
	mes = mes + 1
	if(p > 0 and p < 8000):
		qm = int(input("insira a nova quantidade retirada:"))

if(p <= 0):
	msg = "ZERO"
else:
	msg = "MAXIMO"
print(msg)
print(mes)
	