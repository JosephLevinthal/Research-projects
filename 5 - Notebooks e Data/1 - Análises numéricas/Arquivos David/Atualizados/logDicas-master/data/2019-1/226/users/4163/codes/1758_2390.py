from numpy import*
pm = array(eval(input("quantidade de presentes")))
fm = array(eval(input("quantidade de faltas")))

i = 0 #percorre o vetor
b = 0 #saida
lis = zeros(12, dtype=int)
while(i<size(pm)):
	lis[i] = pm[i]-fm[i] 
	b = b +1
	i = i +1
	
l = 0
while (l < size(lis)):
	if (lis[l] != max(lis)):
		l = l + 1
	else:
		msg = (l+1)
		l = l + 1
print(msg)
			
   
		
		