from numpy import*
mat = array(eval(input("Matriz: ")))

a = mat[1, 2]
for i in range(shape(mat)[0]):
	for j in range(shape(mat)[1]):
		if (i != j):
			if a > mat[i,j]:
				a = a
			elif a < mat[i,j]:
				a = mat[i,j]
print(a)
			
		