# Ao testar sua solução, não se limite ao caso de exemplo.

x = float(input("digite o x: "))
y = float(input("digite o y: "))

if (x!=0)and(y==0):
	print("Eixo X")
else:
	if (y!=0) and(x==0):
		print("Eixo Y")
	else:
		if(y==0)and(x==0):
			print("Origem")
		else:
			if(x>0)and(y>0):
				print("Q1")
			else:
				if(x>0)and(y<0):
					print("Q4")
				else:
					if(x<0)and(y>0):
						print("Q2")
					else:
						if(x<0)and(y<0):
							print("Q3")