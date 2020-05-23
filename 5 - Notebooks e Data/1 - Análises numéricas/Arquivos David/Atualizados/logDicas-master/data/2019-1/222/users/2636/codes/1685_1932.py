p1a = float(input())
p1b = float(input())
p2a = float(input())
p2b = float(input())
p3a = float(input())
p3b = float(input())
p1=p1a/p1b
p2=p2a/p2b
p3=p3a/p3b
indexMen=0
vet = [p1,p2,p3]
maior = -99999
menor = 99999
for i in range(1,3):
	if(maior<vet[i]):
		maior=vet[i]
		index=i
	if(vet[i]<menor):
		menor = vet[i]
		indexMai=i
for i in vet:
	if(i!=maior and i!=menor):
		mid = i
if(vet[0]==maior):
	if(vet[1]>vet[2]):
		print("2 e 3")
	elif(vet[2]>vet[1]):
		print("3 e 2")
if(vet[1]==maior):
	if(vet[0]>vet[2]):
		print("1 e 3")
	elif(vet[2]>vet[0]):
		print("3 e 1")
if(vet[2]==maior):
	if(vet[0]>vet[1]):
		print("1 e 2")
	elif(vet[1]>vet[0]):
		print("2 e 1")