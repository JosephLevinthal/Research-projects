var1=float(input("x:"))
var2=float(input("y:"))

if(var1==0 and var2==0):
	print("Origem")
elif((var1==0) and (var2>0 or var2<0)):
	print("Eixo Y")
elif((var1>0 or var1<0) and var2==0):
	print("Eixo X")
elif(var1>0 and var2>0):
	print("Q1")
elif(var1>0 and var2<0):
	print("Q4")
elif(var1<0 and var2>0):
	print("Q3")
elif(var1<0 and var2<0):
	print("Q2")
