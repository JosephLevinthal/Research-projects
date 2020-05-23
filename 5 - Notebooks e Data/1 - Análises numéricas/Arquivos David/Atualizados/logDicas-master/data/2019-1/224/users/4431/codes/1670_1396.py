x=float(input("Digite o valor consumido: "))
if(x>300):
	y=x-(x*0.94)
	z=x+y
else:
	y=x*0.1
	z=x+y
print(round(z,2))	

			