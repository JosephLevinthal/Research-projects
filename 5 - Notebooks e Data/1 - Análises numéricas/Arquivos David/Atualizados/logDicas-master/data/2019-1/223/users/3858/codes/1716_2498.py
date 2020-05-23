a = int(input())
b = int(input())
perc_a = float(input())
perc_b = float(input())

pop_a = a
pop_b = b
anos= 0
while(pop_a<pop_b):
	cresa = pop_a * (perc_a/100)
	cresb = pop_b * (perc_b/100)
	pop_a = cresa + pop_a
	pop_b = cresb + pop_b
	anos = anos + 1
	
print(anos)
	