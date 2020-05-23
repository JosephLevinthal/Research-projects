ha = int(input("A"))
hb = int(input("B"))
pca = float(input("Percentual A: "))
pcb = float(input("Percentual B: "))

ano = 0

while(ha<hb):
	ha = ha + ha * pca/100
	hb = hb + hb * pcb/100
	ano = ano + 1
print(ano)