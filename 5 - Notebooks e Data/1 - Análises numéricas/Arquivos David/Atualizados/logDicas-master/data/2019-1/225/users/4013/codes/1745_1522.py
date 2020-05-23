q1 = int(input("quantidade inicial:"))
dm = int(input("despesa mensal:"))
qm = int(input("quantidade coletada por mes:"))
qr = int(input("quantidade roubada:"))

acum = q1
cont = 0

while (cont < acum):
	acum = acum + -dm + qm - qr
	cont = cont + 1

print(cont)