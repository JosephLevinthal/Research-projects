x=float(input("Digite a sua altura:"))
y=float(input("Digite a altura do seu amigo: "))
if(x>1.37 and y>1.37):
	print("Sim")
else:
	if(x>1.37 and y<1.37):
		print("Sim")
	else:
		if(x<1.37 and y>1.37):
			print("Sim")
		else:
			print("Nao")

if(x>y):
	print(x)
else:
	print(y)
	