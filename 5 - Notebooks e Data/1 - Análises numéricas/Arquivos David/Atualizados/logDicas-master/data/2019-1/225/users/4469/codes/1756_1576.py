from numpy import*

v1 = array(eval(input()))
v2 = array(eval(input()))

p = 0
e = 0
b = 0

while(p < size(v1) and p < size(v2)):
	if(v1[p] == v2[p]):
		e = e + 1
		b = b + 1
	elif(v1[p] == 33 and v2[p] == 22) or (v1[p] == 22 and v2[p] == 11) or (v1[p] == 11 and v2[p] == 33):
		e = e + 1
	elif(v2[p] == 33 and v1[p] == 22) or (v2[p] == 22 and v1[p] == 11) or (v2[p] == 11 and v1[p] == 33):
		b = b + 1
		
	p = p + 1

print(size(v1))

if(e > b):
	print("EUSAPIA")
elif(b > e):
	print("BARSANULFO")
else:
	print("EMPATE")