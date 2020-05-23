from numpy import*
a = float(input("Aceleracao:"))
v0 = float(input("Velocidade:"))
num = int(input("Entre com o numero:"))
i = 0 
t = arange(num)
d = zeros(num)

while (i<size(t)):
	d[i]= a*t[i]**2 /2. + v0*t[i]
	
	i= i+1
print(d)