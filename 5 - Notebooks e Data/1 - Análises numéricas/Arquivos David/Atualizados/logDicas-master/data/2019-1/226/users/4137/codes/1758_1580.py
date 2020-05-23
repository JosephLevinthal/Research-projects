from numpy import*

x = array(eval(input("Notas dos alunos:")))
y = array(eval(input("Nomes dos alunos:")))

i = 0 #posição no vetor 
p = 0 #aprovados
f = 0 #faltas
r = 0 #alunos reprivados
m = max(x)
k = 0 #posição do numero maximo
z = 0
while(i < size(x)):
	if(x[i] == -1):
		f = f + 1
		i = i + 1
	elif(x[i] >= 6):
		p = p + 1
		i = i + 1
	elif(x[i]>=0 and x[i] < 6):
		r = r + 1
		i = i + 1

while(max(x)!= x[z]):
	k = k + 1
	z = z + 1

media = sum(x) + f
div = size(x) - f
n = round(media/div , 2)
print(f)
print(p)
print(r)
print(n)
print(y[k])