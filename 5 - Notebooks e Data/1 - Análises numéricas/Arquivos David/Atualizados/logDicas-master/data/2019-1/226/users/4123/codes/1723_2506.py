qi = int(input())
pc = float(input())/100
qr = int(input())
i = 0

while 0<qi<12000:
	qi += qi*pc - qr
	i+=1
if qi<0:
	print("EXTINCAO")
	print(i)
else:
	print("LIMITE")
	print(i)