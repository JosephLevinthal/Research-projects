qv= int(input("insira a quantidade de virus no sangue: "))
ql= int(input("insira a quantidade de leucocitos no sangue: "))
pv1= int(input("insira o percentual de multiplicacao dos virus: "))
pl1= int(input("insira o percentual de multiplicacao dos leucocitos: ")) 
av=qv
al=ql
t=0
pv=pv1/100
pl=pl1/100
while (2*av)>al:
	av=av+(av*pv)
	al=al+(al*pl)
	t=t+1
print(t)