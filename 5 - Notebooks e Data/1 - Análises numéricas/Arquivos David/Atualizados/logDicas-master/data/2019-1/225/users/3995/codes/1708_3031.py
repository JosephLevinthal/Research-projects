x=float(input("valor de x:"))
if(x<=1):
	f=round(1, 2)
elif(x>1 and x<=2):
	f=round(2, 2)
elif(x>2 and x<=3):
	f=round((x**2), 2)
else:
	f=round((x**3), 2)
print(f)