from numpy import*
f = array(eval(input("faltas do dia: ")))
seg = 0
ter = 0
qua = 0
qui = 0
sex = 0
sab = 0

for i in range(size(f)):
	if f[i] == 2:
		seg = seg + 1
	elif f[i] == 3:
		ter = ter + 1
	elif f[i] == 4:
		qua = qua + 1
	elif f[i] == 5:
		qui = qui + 1
	elif f[i] == 6:
		sex = sex + 1
	elif f[i] == 7:
		sab = sab + 1

a = seg + ter + qua + qui + sex + sab
p = zeros(6, dtype=float)
for i in p:
	p[0] = round(((seg/a)*100), 1)
	p[1] = round(((ter/a)*100), 1)
	p[2] = round(((qua/a)*100), 1)
	p[3] = round(((qui/a)*100), 1)
	p[4] = round(((sex/a)*100), 1)
	p[5] = round(((sab/a)*100), 1)
				
print(p)
		