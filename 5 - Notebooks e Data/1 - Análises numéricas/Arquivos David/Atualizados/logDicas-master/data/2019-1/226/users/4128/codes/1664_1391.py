kwh = float(input("kwf consumido"))

if(kwh <= 150):
	con = (kwh*0.60) + 5
	print(round(con,2))
else:	
	con = (kwh*0.75) +16
	print(round(con,2))
