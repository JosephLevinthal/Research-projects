from numpy import*


a = input('').split(',')

vet = zeros(5, dtype=int)

for i in range(size(a)):
	if a[i]=='CHN':
		vet[0] = vet[0] + 1
	elif a[i]=='JPN':
		vet[1]=vet[1]+1
 
	elif a[i] == 'KOR':
		vet[2]=vet[2]+1
	elif a[i] == 'MGL':
		vet[3]=vet[3]+1
	elif a[i]== 'THA':
		vet[4]=vet[4]+1
	
print(max(vet))
print(vet)