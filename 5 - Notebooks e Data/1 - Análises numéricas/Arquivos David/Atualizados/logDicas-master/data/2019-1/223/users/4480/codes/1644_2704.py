nota = float(input('nota do fudido do aluno: '))
boni = input()
if(boni=='S'):
	final = nota*1.1
	print(round(final,1))
elif(boni=='N'):
	print(nota)