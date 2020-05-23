tempo=int(input("tempo"))

if(tempo<=200):
	custo=5000+(100*tempo)
	print(custo)
else:
	custot=8000+(100*200)+90*(tempo-200)
	print(custot)