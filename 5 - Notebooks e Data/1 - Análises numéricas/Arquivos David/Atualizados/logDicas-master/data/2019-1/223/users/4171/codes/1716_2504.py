# qic > qil || percv < percl

qiv = int(input("Qtd inicial de copias do virus: "))
qil = int(input("Qtd inicial de leucocitos: "))
percv = int(input("% * virus: "))
percl = int(input("% * leucocitos: "))


qv = 0 #acumuladora qtd virus
ql = 0 #acumuladora qtd leucocitos
d = 0 #contadora dias transcorridos
diarial = qil 
diariav = qiv 

while diarial <= 2*diariav:
	
	rendv = diariav * percv/100
	diariav = diariav + rendv
	
	rendl = diarial * percl/100
	diarial = diarial + rendl
	
	
	
	d += 1
	
	
print(d)