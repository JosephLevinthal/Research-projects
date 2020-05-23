qi = int(input("Digite a quantidade inicial de grifos: "))
qx = int(input("Digite a quantidade de novos grifos: "))
qy = int(input("Digite a quantidade de grifos contaminados a cada trimestre: "))

gp = 0
t = 3
c = 0

while qi + qx != 400 and qy == qi + qx:
	t = (t * qx) + qi - (t * qy)
	gp = gp + 1 
	c = c + 1
print(t)
	