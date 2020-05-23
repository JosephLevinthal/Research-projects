from numpy import*
vet = array(eval(input("")))
a = []
for i in vet:
	if i%2==1:
		a.append(i)
print(str(a).replace(',',''))
