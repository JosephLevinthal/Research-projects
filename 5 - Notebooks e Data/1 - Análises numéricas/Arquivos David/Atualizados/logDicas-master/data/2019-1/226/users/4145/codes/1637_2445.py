m = input("modelo de conversao: ")
t = float(input("temperatura: "))

if(m.lower() == "c"):
	f = 9*t/5 + 32 
	print(f)
else:
	c = 5/9*(t - 32)
	print(c)
	