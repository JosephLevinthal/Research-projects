x = input("insira o nome:")

if(x[0] >= "A" and x[0] <= "K"):
	print(x,"vai para a sala",101)
elif(x[0] > "K" and x[0] <= "N"):
	print(x,"vai para a sala",102)
else:
	print(x,"vai para a sala",103)