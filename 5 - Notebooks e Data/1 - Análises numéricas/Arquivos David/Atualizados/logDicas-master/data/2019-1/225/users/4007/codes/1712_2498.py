a = int(input("numero de habitantes: "))
b = int(input("numero de habitantes: "))
pca = float(input("percentual a: "))
pcb = float(input("percentual b:"))
pca = pca/100
pcb = pcb/100
ano = 0
while(a < b):
	b = b * pcb + b
	a = a * pca + a
	ano = ano + 1
print(ano)
	
		  

	 	
	