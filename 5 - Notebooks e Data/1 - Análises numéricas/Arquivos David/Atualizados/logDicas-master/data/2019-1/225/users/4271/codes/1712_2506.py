Qi = int(input(""))
Pc = float(input(""))
Qv = int(input(""))

Max = 12000
anos = 0

while 0 < Qi <= Max: 
	Qi = Qi + Qi*(Pc/100) - Qv
	anos = anos + 1
if Qi >= Max:
	print("LIMITE")
elif Qi < 0:
	print("EXTINCAO")
print(anos)