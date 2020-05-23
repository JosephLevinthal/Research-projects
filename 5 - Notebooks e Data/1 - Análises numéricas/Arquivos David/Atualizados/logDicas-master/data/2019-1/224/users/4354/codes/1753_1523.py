qi = int(input("quantidade de baloes: "))
qc = int(input("quantidade nova de baloes: "))
qd = int(input("quantidade de baloes destruidos: "))
t = 0
while(qi<200):
	qi = qi + (qc - qd)
	t = t + 1
print(t)
	