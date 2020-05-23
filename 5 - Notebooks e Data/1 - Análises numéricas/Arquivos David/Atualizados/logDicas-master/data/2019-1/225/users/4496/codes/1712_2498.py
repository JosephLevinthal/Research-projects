NA = int(input("Habitantes da cidade A: "))
NB = int(input("Habitantes da cidade B: "))
PA = float(input("crescimento populacional A: "))
PB = float(input("crescimento populacional B: "))

cna=NA+((NA*PA)/100)
cnb=NB+((NB*PB)/100)
ct=1

while(cna<cnb):
	cna=cna+((cna*PA)/100)
	cnb=cnb+((cnb*PB)/100)
	ct=ct+1
print(ct)