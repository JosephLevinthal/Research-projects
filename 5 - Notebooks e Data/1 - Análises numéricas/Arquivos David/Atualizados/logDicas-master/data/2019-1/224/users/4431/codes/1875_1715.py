from numpy import*
t=array(eval(input("Digite a tabela: ")))
y=int(input("Digite o numero de linha: "))
z=int(input("Digite o numero de coluna: "))
if(t[y,z]=="N"):
	print("FOGO")
elif(t[y,z]=="L"):
	print("AGUA")