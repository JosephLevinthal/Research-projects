from numpy import*
x = array(eval(input("insira o numero de termos; ")))
y = array(eval(input("insira o numero de termos; ")))
a = 0
r = 0
i = 0
f = 0
s = 0
soma = 0
l = 0



while(i<size(x)):
	if(x[i]<0): #alunos que faltaram
		f =  f + 1
		
	elif(x[i]>=0): #media dos alunos presentes
		soma = soma + x[i]
		s = s + 1
		
		if(x[i]>=6):
			a = a + 1
		elif(x[i]<6):
			r = r + 1
	i = i + 1

media = soma / (size(x) - f)		
			
print(f) #falta
print(a) #aprovados
print(r) #reprovados
print(round(media, 2)) #media



while (l < size(x)):
	if (x[l] != max(x)):
		l = l + 1
	else:
		msg = (y[l])
		l = l + 1
print(msg)
		

		

