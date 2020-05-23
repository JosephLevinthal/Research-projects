n = int(input("serie: "))
t = 0
pi = 0
while (t<n):
	if (t%2 == 0):
		pi = pi + 1/((1+(2*t))*(3**t)) 
		t = t + 1
	else: 
		pi = pi - 1/((1+(2*t))*(3**t))
		t = t + 1
pi = pi*(12**0.5)
print(round(pi, 8))