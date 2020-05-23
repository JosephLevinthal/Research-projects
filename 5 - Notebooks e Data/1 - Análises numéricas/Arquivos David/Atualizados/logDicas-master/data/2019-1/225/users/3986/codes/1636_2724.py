n1=int(input("numero 1: "))
n2=int(input("numero 2: "))
n3=int(input("numero 3: "))
x=max(n1,n2,n3)
y=min(n1,n2,n3)
v=n1 + n2+ n3 -x -y
if (n1 != n2 != n3) :
	print(v)

else :
	print("Nao tem solucao")
