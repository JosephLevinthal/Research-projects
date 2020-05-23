s= float(input("escreva o salario: "))
c=0
if(s<=1659.38):
	c=c+(s-(s*8/100))
if(s>=1659.39) and (s<=2765.66):
	c=c+(s-(s*9/100))
if(s>=2765.67) and (s<=5531.31):
	c=c+(s-(s*11/100))
if(s>5531.31):
	c=c+(s-608.44)
t=0
if(c<=1903.98):
	t=t+c
if(c>=1903.99) and (c<=2826.65):
	t=t+(c-(c*(7.5/100)))
if(c>=2826.66) and (c<=3751.05):
	t=t+(c-(c*(15/100)))
if(c>=3751.06) and (c<=4464.68):
	t=t+(c-(c*(22.5/100)))
if(c>4464.68):
	t=t+(c-(c*(27.5/100)))
T=round(t,2)
print("Salario liquido = R$" + T)
