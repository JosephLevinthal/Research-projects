# Ao testar sua solução, não se limite ao caso de exemplo.
x = float(input())
y = float(input())

if x>0 and y>0:
	print("Q1")
elif x<0 and y>0:
	print("Q2")
elif x<0 and y<0:
	print("Q3")
elif x>0 and y<0:
	print("Q4")
elif x==y==0:
	print("Origem")
elif x==0:
	print("Eixo Y")
else:
	print("Eixo X")