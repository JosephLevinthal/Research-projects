h = hf = float(input())
i = 0
while h - 0.5*9.8*i**2>0:
	hf = h - 0.5*9.8*i**2
	print("t = ",i)
	print("h = ",round(hf,1))
	i+=1