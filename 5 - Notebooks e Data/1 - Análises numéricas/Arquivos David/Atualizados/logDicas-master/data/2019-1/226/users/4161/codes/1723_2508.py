n = int(input("serie: "))
t = 1
x = 3
if n == 1:
	x = 3
else:
	while (t<n):
		if (t%2 != 0):
			x = x + 4/((2+2*(t-1))*(3+2*(t-1))*(4+2*(t-1)))
			t = t + 1
		else:
			x = x - 4/((2+2*(t-1))*(3+2*(t-1))*(4+2*(t-1)))
			t = t + 1
print(round(x,8))