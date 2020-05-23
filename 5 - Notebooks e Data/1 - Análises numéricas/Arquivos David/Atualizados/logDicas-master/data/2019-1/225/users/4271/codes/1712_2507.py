Qi = int(input(""))
Pc = float(input(""))
Qv = int(input(""))

Max = 8000
meses = 0

while 0 < Qi <= Max: 
	Qi = Qi + Qi*(Pc/100) - Qv
	meses = meses + 1
if Qi >= Max:
	print("MAXIMO")
elif Qi < 0:
	print("ZERO")
print(meses)