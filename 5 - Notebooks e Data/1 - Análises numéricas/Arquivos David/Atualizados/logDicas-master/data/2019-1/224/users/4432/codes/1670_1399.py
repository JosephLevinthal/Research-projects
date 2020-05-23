qva=float(input("quantidade de votos abocio"))
qvb=float(input("quantidade de votos bemelza"))
z=qva+qvb
x=qvb/z*100
y=qva/z*100
if(qva>qvb):
	print("Ambrosio Rutra")
	print(round(y,2))
else:
	print("Demelza Olecram")
	print(round(x,2))
	