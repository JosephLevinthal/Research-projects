habA = int(input("Habitantes: "))
habB = int(input("Habitantes: "))
cresA = float(input("Crescimento: "))
cresB = float(input("Crescimento: "))
t = 0
popA = habA
popB = habB

while (popA < popB):
	t = t + 1
	popA = popA * cresA/100 + popA
	popB = popB * cresB/100 + popB
	
	
print(t)	
	

	