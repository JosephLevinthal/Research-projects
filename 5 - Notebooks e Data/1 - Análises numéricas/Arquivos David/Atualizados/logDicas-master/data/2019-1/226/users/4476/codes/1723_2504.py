qicv = int(input("digite o valor: "))
qils = int(input("digite o valor: "))
mv = int(input("digite o valor: "))
ml = int(input("digite o valor: "))

permv = mv/100
perml = ml/100

d = 0

while (qils<=2*qicv): 
	qicv = qicv + (qicv*permv)
	qils = qils + (qils*perml)
	d = d + 1
print(d)