from numpy import*

qt = array(eval(input("Alunos por sala: ")))
tp = 0 

#Primeira parte - ok
for x in qt:
	if(x%5 == 0):
		tp = tp + 1
print(tp)
	
#Segunda parte
u = zeros(tp, dtype=int)
i = 0
t = 0

while(i < size(qt)):
	if(qt[i]%5 == 0):
		u[t] = u[t] + i
	i = i + 1
		
print(u)
	