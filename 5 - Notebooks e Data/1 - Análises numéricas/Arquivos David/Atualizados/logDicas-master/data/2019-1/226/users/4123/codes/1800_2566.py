from numpy import*
vet = array(eval(input()))
n = zeros(6, dtype = float)
i = 0
for x in vet:
	n[x-2]+=1
for i in range(0,6):
	n[i] = round(n[i]/size(vet)*100,1)
print(n)