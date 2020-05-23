n1 = int(input("primeiro: "))
n2 = int(input("segundo: "))
n3 = int(input("terceiro: "))

if(n1<n2, n1<n3):
	menor = n1
	
if(n2<n3, n2<n1):
	menor = n2

	
if(n3<n1, n3<n2):
	menor = n3
	
	
print(menor)
