area= float(input("area a ser fertilizada em hectares"))
if (area <= 10000):
	custo=area*5
else:
	custo=50000+((area-10000)*4)
print(round(custo, 2))