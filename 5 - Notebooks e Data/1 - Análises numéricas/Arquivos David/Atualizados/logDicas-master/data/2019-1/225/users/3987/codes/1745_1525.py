vo = int(input(":"))
vb = int(input(":"))
vr = int(input(":"))

i = 0

while(vo > 1000):
	vo = vo + ((vo + vb)- vr)
	i = i + 1
print(i)