val = float(input("digite valor consumido "))

if val <= 300:
	gorjeta = (val * 10 / 100)
else:
	gorjeta = (val * 6 / 100)

print (round(val + gorjeta, 2))