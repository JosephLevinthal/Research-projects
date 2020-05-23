a = float(input("altura:"))
s = input("sexo:")
M = "s"
if(s.upper() == "M"):
	msg = (72.7 * a) - 58.0
else:
	msg = (62.1 * a) - 44.7

r = round(msg, 2)

print(r)