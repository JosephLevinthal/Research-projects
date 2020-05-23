var=input("nome do ataque:")
var2=int(input("dado1:"))
var3=int(input("dado2:"))
fi=10+(var2+var3)
ga=6+(var2+var3)
tm=(var2+var3)**2

if(var=="FURIA"):
	  print(fi)
elif(var=="GRITO"):
	  print(ga)
elif(var=="TOQUE"):
	  print(tm)
elif((var!="FURIA") and (var!="GRITO") and (var!="TOQUE")):
	print("Entrada invalida")
