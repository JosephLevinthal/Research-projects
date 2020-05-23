from  numpy import*

vet = array(eval(input("Vetor")))
lol = size(vet)
q = 0
for i in vet:	
	if (i <= 50):
		q += 1 
print(q)		
sub = zeros( q , dtype=int)

l = 0 
for i in  range(size(vet[q+1])):
	bu = 0
	if i <= 50:
		
		sub[l] = sub[l] + l
		l += 1
		bu = bu + l
		
		
		print(sub)
		


	

