a = float(input("type the height: "))
s = input("m ou f: ")
f_h = (72.7*a)-58
f_m = (62.1*a)-44.7

if s == "M".upper():
	print(round(f_h, 2))
else:
	print(round(f_m, 2))