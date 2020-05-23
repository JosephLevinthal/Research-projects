from numpy import*
danos = array(eval(input("danos de ataque: ")))
i = 0 # contador do laço
p = danos[i] * 1 # peso de ataque
acum = 0 #acumuladora de danos

while(i < size(danos)):
	danos = danos[i]*p
	acum = acum + danos
	i = i + 1
	p = p + 1
print(acum)