pgI = int(input())
vmI = int(input())
percP = float(input())/100
percV = float(input())/100

pgI2 = pgI
vmI2 = vmI
acP = 0
acV = 0
anos = 0
ct = 0

while ct <= 80000:
	
	pgI2 += pgI2 * percP
	acP = pgI2
	
	vmI2 += vmI2 * percV
	acV = vmI2
	
	ct = acV+acP
	
	anos += 1
	
print(anos)