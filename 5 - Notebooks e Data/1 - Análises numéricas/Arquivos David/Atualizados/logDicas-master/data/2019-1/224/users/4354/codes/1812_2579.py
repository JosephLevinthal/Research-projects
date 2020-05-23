calc = input("digite Calcule: ")
if(calc == "Calcule"):
	b = 1
	h = 0
	for i in range(50):
		h = h + b/(i+1)
		b = b + 2
print(round(h,2))