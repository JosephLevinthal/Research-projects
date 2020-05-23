x = int(input("numero inteiro:"))
e = 0
d = 0
y = 0
f = 0
q = 0
i = 0
while(x != 0):
	if(x%2 == 0):
		y = x + y 
		i = i + 1
		d = y / i
	else:
		q = x + q
		f = f + 1
		e = q / f
	x = int(input("numero inteiro:"))

print(round(d,2))
print(round(e,2))