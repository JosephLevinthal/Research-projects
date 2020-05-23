a = int(input("numero de hab. a: "))
b = int(input("numero de hab. b: "))
pa = float(input("percentual de a: "))
pb = float(input("percentual de b: "))

t = 0

while(a <= b):
	popa = a + (a * pa / 100)
	popb = b + (b * pb / 100)
	tempo = t + 1
	print(tempo)	

