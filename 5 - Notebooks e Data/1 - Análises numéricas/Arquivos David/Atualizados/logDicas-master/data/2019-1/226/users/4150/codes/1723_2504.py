qv = int(input("copias do virus de micalateia: "))
ql = int(input("quantidade de leucovitos no sangue: "))
pcv = int(input("percentual de multiplicao diaria do virus: "))
pcl = int(input("percentual de multiplicacao diaria dos leucocitos: "))

dia = 0 

while(ql <= 2*qv):
	qv = qv + (qv *(pcv/100)) # acumuladora
	ql = ql + (ql *(pcl/100)) # acumuladora
	dia = dia + 1
	
print(dia)