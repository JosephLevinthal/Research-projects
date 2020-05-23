caso = input("Qual caso? (C/F)")

if(caso == "c".upper()):
	f = float(input("qual a temperatura? "))
	cel = (f*(9/5)) + 32
	print(round(cel, 2))
	
else:
	c = float(input("qual a temperatura? "))
	f = (5/9)* (c - 32)
	print(round(f, 2))
	
