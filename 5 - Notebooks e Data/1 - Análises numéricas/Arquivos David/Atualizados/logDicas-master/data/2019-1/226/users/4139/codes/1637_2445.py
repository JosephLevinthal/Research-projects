t = input("medida de temperatura C ou F:")
a = float(input("escala da temperatura:"))

if ("C" == t): 
	r = (a*9/5)+32
	
else:
	r = (a - 32)*5/9
	
print(round(r,2))