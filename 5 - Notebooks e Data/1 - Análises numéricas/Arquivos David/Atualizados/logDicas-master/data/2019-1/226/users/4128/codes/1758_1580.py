from numpy import*

n = array(eval(input("Notas: ")))
a = array(eval(input("Alunos: ")))

soma = 0
i = 0 #contadora
f = 0 #faltas
ap = 0 #aprovados
re = 0 #reprovados
while(i != size(n)):
	if(n[i] == -1):
		f = f + 1
	elif(n[i] >= 6):
		ap = ap + 1
	elif(n[i] < 6) and (n[i] != -1):
		re = re + 1
	if(n[i] != -1):
		soma = soma + n[i]
	if(n[i] == max(n)):
		m = i
	i = i +1
print(f) 
print(ap)
print(re)
print(round(soma/(size(n)-f),2))
print(a[m])