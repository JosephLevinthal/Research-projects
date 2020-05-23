virus = int(input("qntd inicial de virus: "))
leuc = int(input("qntd inicial de leucocitos: "))
taxa_v = int(input("percentil de virus: "))/100
taxa_l = int(input("percentil de leucocitos: "))/100


dias = 0
while(virus>leuc/2):
	virus = virus + (virus * taxa_v)
	leuc = leuc + (leuc*taxa_l)
	dias=dias+1
print(dias)
