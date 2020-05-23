ntr = int(input("Digte o numero de termos desejados: "))

an = 1
bn = 1/2**0.5
tn = 0.25
pn = 1
i = 0
while(i < ntr):
	a = an
	b = bn
	t = tn
	p = pn
	pi = ((a+b)**2)/(4*t)
	an = (a + b)/2
	bn = (a*b)**0.5
	tn = t - p*(a - an)**2
	pn = 2*p
	i = i+1
	print(round(pi, 14))
