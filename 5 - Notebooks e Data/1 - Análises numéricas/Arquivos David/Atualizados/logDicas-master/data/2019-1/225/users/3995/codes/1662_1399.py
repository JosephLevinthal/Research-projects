v1=int(input("Quantidade para A.R:"))
v2=int(input("Quantidade para D.O:"))
if(v1>v2):
	print("Ambrosio Rutra")
	h=(v1/(v1+v2))*100
	print(round(h, 2))
else:
	print("Demelza Olecram")
	h=(v2/(v1+v2))*100
	print(round(h, 2))
	
	