qic=float(input(""))
qil=float(input(""))
percV=float(input(""))
percL=float(input(""))
day=0
while(qil< 2*qic):
	qic= qic*(percV/100)+qic
	qil= qil*(percL/100)+qil
	day+=1
print(day)