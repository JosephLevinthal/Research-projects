from numpy import*
nota=array(eval(input("entre com as notas dos alunos:")))

while(size(nota)>2):
	i=0
	for elemento in nota:
		if(elemento>=5 and elemento<7):
			i = i + 1
			
	print(i)
	nota=array(eval(input("entre com as notas dos alunos:")))