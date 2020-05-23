ha = int(input(""))
hb = int(input(""))
pa = float(input(""))
pb = float(input(""))

pca = pa / 100
pcb = pb / 100

ano = 0 

while(ha < hb):
	ha = ha + (ha * pca)
	hb = hb + (hb * pcb)
	ano = ano + 1 
	
print(ano)