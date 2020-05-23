Qv = int(input(""))
Ql = int(input(""))
Pv = float(input(""))
Pl = float(input(""))

dias = 0
while Ql <= 2*Qv:
	Ql = Ql + Ql*(Pl/100)
	Qv = Qv + Qv*(Pv/100)
	dias = dias + 1
print(dias)