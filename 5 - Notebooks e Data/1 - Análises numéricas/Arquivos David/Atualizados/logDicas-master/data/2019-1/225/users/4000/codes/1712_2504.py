qv = int(input("qtde de virus no sangue: "))
ql = int(input("qtde de leucocitos no sangue: "))
pv = float(input("percentual de virus  no sangue: "))
pl = float(input("percentual de leucocitos no sangue: "))
qtv = qv
qtl = ql
t = 0
while(qtl < 2*qtv):
	qtv = qtv + ((qtv * pv)/100)
	qtl = qtl + ((qtl * pl)/100)
	t= t+1
print(t)