h = float(input("altura: "))
s = input("M/F ")
if (s == "M" ):
	pi = 72.7 * h - 58
	print(round(pi, 2))
elif(s == "F"):
	pi =62.1 * h - 44.7
	print(round(pi, 2))