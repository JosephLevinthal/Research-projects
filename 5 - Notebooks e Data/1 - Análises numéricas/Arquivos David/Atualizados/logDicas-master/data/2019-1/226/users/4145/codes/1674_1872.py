# Ao testar sua solução, não se limite ao caso de exemplo.
x = float(input("valor do eixo x: "))
y = float(input("valor do eixo y: "))
if(x==y==0):
	print("Origem")
elif((x==0)and(y!=0)):
	print("Eixo Y")
elif((x!=0)and(y==0)):
	print("Eixo X")
elif((x>0)and(y>0)):
	print("Q1")
elif((x>0)and(y<0)):
	print("Q4")
elif((x<0)and(y>0)):
	print("Q3")
else:
	print("Q2")
#((x<0)and(y<0)):
	#print("Q2")
