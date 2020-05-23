nha= float(input("insira a quantidade de habitantes da city A: "))
nhb= float(input("insira a quantidade de habitantes da city B: "))
pca= float(input("insira o percentual de crescimento populacional da cidade A: "))
pcb= float(input("insira o percentual de crescimento populacional da cidade b: "))
ha=nha
hb=nhb
t=0
b=pca/100
d=pcb/100
while (ha<hb):
	ha=ha+(ha*b)
	hb=hb+(hb*d)
	t=t+1
print(t)