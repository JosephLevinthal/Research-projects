e= input("insira V para vitoria, D para derrota ou E para empate: ").upper()
d=0
s=0
while e!="X":
	if e=="V" or e=="D" or e=="E":
		if e=="V":
			p=3
		if e=="D":
			p=1
		if e=="E":
			p=2
		s=p+s
		d=d+1
	e= input("insira V para vitoria, D para derrota ou E para empate: ").upper()
r=s*100/(d*3)
print(round(r,2))