N= int(input("Insira a capacidade do navio:"))
e= int(input("Insira o estoque inicial de containers:"))
Q= int(input("Insira a quantidade Q de containers que chegam ao deposito:"))

q=e
semanas=0

while(q>0):
	q=q-N+Q
	
	semanas=semanas+1
print(semanas)
