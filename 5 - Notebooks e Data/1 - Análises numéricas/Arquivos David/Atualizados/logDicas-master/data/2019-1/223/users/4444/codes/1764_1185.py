from numpy import *
vetor=array(eval(input('Digite:')))

i=0
q_diabeticos=0		

while(i<len(vetor)):
		if(vetor[i]>99):
			print(i)
			q_diabeticos= q_diabeticos+1
		i=i+1
print(q_diabeticos)	
		
		
				
		

							  
			