na = int(input("num. Hab: "))
nb = int(input("num. Han: "))
pa = float(input("perc. cresA: "))
pb = float(input("perc. cresb: "))

percA = pa / 100
percB = pb / 100

ano = 0
while(na < nb):
	na = na + (na * percA)
	nb = nb + (nb * percB)
	ano = ano + 1
print(ano)