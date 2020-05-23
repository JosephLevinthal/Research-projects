A = int(input(""))
B = int(input(""))
Pa = float(input(""))
Pb = float(input(""))

x = 0

while A < B:
        A = (A + A * (Pa/100))
        B = (B + B * (Pb/100))
        x = x  + 1

print(x)
	