from numpy import*

a = array(eval(input("valores: ")))

i = 0

while (i<size(a)):
	if a[i] > 80:
		desconto = a[i]*0.15
		valor = a[i]- desconto
	else:
		valor = a[i]
		
print(sum(a[i]), 2)
		

	

	
	