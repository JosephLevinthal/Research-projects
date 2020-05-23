from numpy import*
f= array(eval(input("vetor numero de faltas: ")))
fd=zeros(6, dtype=int)
i= 0
for v in f:
	if f[i]== 2:
		fd[0]= fd[0] + 1
		i =i + 1
	elif f[i]== 3:
		fd[1]= fd[1] + 1
		i = i + 1
	elif f[i]==4:
		fd[2]= fd[2] + 1
		i = i + 1
	elif f[i]==5:
		fd[3]= fd[3] + 1
		i = i + 1
	elif f[i]==6:
		fd[4]= fd[4] + 1
		i = i + 1
	elif f[1]==7:
		fd[5]= fd[5] + 1
		i = i + 1
pf= zeros()
print(pf)