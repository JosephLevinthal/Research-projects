#saida tempo que vai ser o meu contador em cada segundo
#altura no segundo 
#round 1 
Ho=float(input())
i=0
H=Ho-(1/2)*9.8*i**2
while(H>=0):
	
	
	print("t =",i)
	
	print("h =",round(H,1))
	
	i=i+1
	H=Ho-(1/2)*9.8*i**2
	
	