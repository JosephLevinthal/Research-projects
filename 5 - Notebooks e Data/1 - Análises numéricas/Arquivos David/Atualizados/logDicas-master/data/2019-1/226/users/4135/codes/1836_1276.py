from numpy import*

mat=array(eval(input("Digite a matriz: ")))
funcionarios= mat.shape[1]

total=zeros(funcionarios,dtype=int)

for j in range(funcionarios):
	total[j]=sum(mat[:,j])
big=max(total)


if(big==total[0]):
	print(1)
elif(big==total[1]):
	print(2)
elif(big==total[2]):
   print(3)
elif(big==total[3]):
	print(4)
elif(big==total[4]):
   print(5)
elif(big==total[5]):
   print(6)
elif(big==total[6]):
   print(7)
		

