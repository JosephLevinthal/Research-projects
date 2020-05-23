b=input("qual escala?")
a=float(input("valor da temperatura:"))
if(b.upper( )=="c"):
	eq=a*(9/5)+32
else:
	eq=(a-32)*(5/9)
print(round(eq,2))