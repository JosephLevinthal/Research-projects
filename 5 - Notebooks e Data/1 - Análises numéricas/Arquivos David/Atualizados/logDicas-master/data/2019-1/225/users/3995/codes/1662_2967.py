var1=float(input("Minha altura: "))
var2=float(input("Altura do amigo: "))
if(var1>=1.37 and var2>=1.37):
	msg="Sim"
if(var1>=1.37 and var2<1.37):
	msg="Sim"
if(var1<1.37 and var2>=1.37):
	msg="Sim"
if(var1<1.37 and var2<1.37):
	msg="Nao"
print(msg)
if(var1>var2):
	print(var1)
if(var1<var2):
	print(var2)			  