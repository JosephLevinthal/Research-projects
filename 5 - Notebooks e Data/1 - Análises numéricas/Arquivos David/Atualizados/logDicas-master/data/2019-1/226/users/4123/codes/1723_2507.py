qi = int(input())
pc = float(input())/100

i = 0

while 0<qi<8000:
	qr = int(input())
	qi += qi*pc - qr
	i+=1
if qi<0:
	print("ZERO")
	print(i)
else:
	print("MAXIMO")
	print(i)