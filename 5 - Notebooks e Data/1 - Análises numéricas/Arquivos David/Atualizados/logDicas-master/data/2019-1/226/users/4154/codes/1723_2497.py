a  = float(input("Quantia inicial: "))
t = int(input("Tempo de investimento: "))

c=0
while t>c:
	c += 1
	s = a+ a*0.04
	print(round(s,2))
	a = s
	
