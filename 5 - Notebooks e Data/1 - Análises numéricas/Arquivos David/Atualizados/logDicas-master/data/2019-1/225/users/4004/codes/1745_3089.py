x = int(input("movimento inicial da tartaruga: "))

s = 0 #posição

while x != 0:
	s = s + x
	x = int(input("movimento da tartaruga: "))
print(s)
if s > 0:
	print("Direita")
elif s < 0:
	print("Esquerda")
else:
	print("Inicial")