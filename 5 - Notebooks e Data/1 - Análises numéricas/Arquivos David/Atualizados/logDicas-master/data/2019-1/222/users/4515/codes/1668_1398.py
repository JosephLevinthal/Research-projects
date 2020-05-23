tvoo = int(input("Tempo de voo em minutos :"))

if(tvoo <= 200):
	ctotal = 5000+(100*tvoo)
else:	
	ctotal = 8000+(100*200)+(tvoo-200)*90
print(round(ctotal,2))
	
