qi = int(input("quantidade inicial de baloes: "))
qc = int(input("novos baloes: "))
qd = int(input("baloes destruidos: "))
soma = 0 
cont = 0
while (qi < 200):
	qi =  qi + qc - qd 
	cont = cont + 1
print(cont)
	



