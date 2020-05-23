N  = int(input("numero de containers:"))
ei = int(input("estoque inicial:"))
Q = int(input("quantidade Q de containers:"))

v = 7 #viagem
cont = 0 #var acumuladora 
vt = 0 

while (0 < N):
	N = N - (ei + Q)
	cont = (cont + 1) 
print(cont)

