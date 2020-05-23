compra = float(input("valor da compra:"))
if(compra>200):
   total = (-compra/20)+compra
else:
	total = compra
print(round(total,2))