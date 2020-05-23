valorx = float(input("digite o valor para x:"))

if(valorx <= 1):
	valorx = 1
	
elif(valorx > 1 and valorx <= 2):
	valorx = 2
	
elif(valorx > 2 and valorx <= 3):
	valorx = (valorx**2)
	
elif(valorx > 3):
	valorx = (valorx**3)
	
print(round(valorx,2))