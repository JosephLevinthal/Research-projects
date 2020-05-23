qip = int(input("digite o valor: "))
pcm = int(input("digite o valor: "))
prv = int(input("digite o valor: "))

perpcm = pcm/100
m = 0

while ((qip>0) and (qip<8000)):
	qip = qip + (qip*perpcm) - prv
	m = m + 1
	if (qip>=8000):
		print("MAXIMO")
	elif (qip<=0):
		print("ZERO")
	else:
		prv = int(input("digite o valor: "))

print(m)