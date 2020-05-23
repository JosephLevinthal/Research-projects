peso=float(input("leia o peso da encomenda:"))
a=(4999.9)
b=(5000.0)
taxa= round("60,00 2")
if(a<b+taxa):
	excesso= float(round(a+peso)*"0,05 2")
else:
	excesso=float(round(b+peso+taxa)*"0,04 2")
print(excesso)
	
	