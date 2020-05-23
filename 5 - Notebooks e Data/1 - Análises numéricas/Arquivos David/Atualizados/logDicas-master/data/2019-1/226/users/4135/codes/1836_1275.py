from numpy import*

mat=array(eval(input("Dgite a matriz: ")))
funcionarios= mat.shape[0]

total=zeros(funcionarios,dtype=int)

for i in range(funcionarios):
	total[i]=sum(mat[i,:])

print(total)


