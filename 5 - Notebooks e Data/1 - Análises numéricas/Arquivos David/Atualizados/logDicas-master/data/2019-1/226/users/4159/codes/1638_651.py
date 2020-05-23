h = float(input("altura: "))
sex = (input("e menino ou menina? (M/F) ")).upper()
if(sex=="M"):
	p = (72.7*h)-58
else:
	p = (62.1*h)-44.7
print(round(p, 2))
