a = int(input())
b = int(input())
pa = float(input())
pb = float(input())

pop_a = a
pop_b = b
anos= 0
while(pop_a<pop_b):
	cresa = pop_a * (pa/100)
	cresb = pop_b * (pb/100)
	pop_a = cresa + pop_a
	pop_b = cresb + pop_b
	anos = anos + 1
	
print(anos)
	