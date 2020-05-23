ha = int(input())
nb = int(input())
pa = float(input())
pb = float(input())

cna = na + ((na * pa) / 100)
cnb = nb + ((nb * pb) / 100)
ct = 1

while(cna < cnb):
	cna = cna + ((cna * pa) / 100)
   cnb = cnb + ((cnb * pb) / 100)
	ct = ct + 1
	
print(ct)
	