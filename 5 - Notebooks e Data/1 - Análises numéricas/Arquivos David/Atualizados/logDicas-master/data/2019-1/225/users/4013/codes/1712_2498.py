na = int(input("numero de hab da city a:"))
nb = int(input("numero de hab da city b:"))
pa = float(input("percentual da city a:"))
pb = float(input("percentual da city b:"))

cont = 0

while(na < nb):
	na = na + (na *pa/100)
	nb = nb + (nb * pb/100)
	cont = cont + 1
print(cont)