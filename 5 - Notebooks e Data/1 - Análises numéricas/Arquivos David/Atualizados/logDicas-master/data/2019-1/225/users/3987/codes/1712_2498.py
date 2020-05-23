a = int(input("A:"))
b = int(input("B:"))
c = float(input("C:"))
d = float(input("D:"))

w = a + ((a * c)/100)
q = b + ((b * d)/100)
p = 1 

while(w < q):
	w = w + ((w * c)/100)
	q = q + ((q * d)/100)
	p = p + 1
print(p)
