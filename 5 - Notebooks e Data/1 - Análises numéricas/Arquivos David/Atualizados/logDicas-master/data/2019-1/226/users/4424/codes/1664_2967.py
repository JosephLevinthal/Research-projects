h1=float(input("escreva: "))
h2=float(input("escreva: "))

if(h1 and h2>1.37):
	msg=("Sim")
if(h1 and h2<1.37):
	msg=("Nao")
if(h1>h2):
	x=(h1)
if(h2>h1):
	x=(h2)
	
print(msg)
print(x)