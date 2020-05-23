at = int(input("Altura total: "))
dp = int(input("Distancia percorrida por min: "))
dr = int(input("Distancia regredida por min: "))

subida = 0
minu = 0

while(subida < at):
	subida = subida + dp
	minu = minu + 1
	subida = subida - dr

print(minu)