x= float(input("tempo:"))

if(x<=200):
	print(round((5000+(x*100)),2))
else:
	print(round((8000+20000+(x-200)*90),2))