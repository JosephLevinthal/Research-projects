h = float(input("altura do individuo: "))
s = input("sexo do individuo: ")
pm = round((72.7 * h) - 58,2)
pf = round((62.1*h)-44.7,2)
if(s ==  "M" ):
	print(pm)
else:
	print(pf)
