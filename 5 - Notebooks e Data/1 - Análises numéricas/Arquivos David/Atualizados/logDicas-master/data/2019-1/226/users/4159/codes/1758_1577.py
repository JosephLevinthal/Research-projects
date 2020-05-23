from numpy import*
ac = float(input("aceleracao: "))
vo = float(input("velocidade: "))
n = int(input("tempo: "))
v = arange(n)
t = 0
r = ones(n)
while(t<n):
	d = ((ac*t**2)/2) + vo*t
	r[t] = d
	t = t+1
print(r)