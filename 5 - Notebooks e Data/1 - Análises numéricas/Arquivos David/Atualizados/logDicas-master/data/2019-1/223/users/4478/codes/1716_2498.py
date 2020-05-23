a = float(input("numero de habitantes cidade A: "))
b = float(input("numero de habitantes cidade B: "))
c = float(input("percentual de crescimento city A: "))/100
d = float(input("percentual de crescimento city B: "))/100


anos = 0
while(a<b):
	a = a + (a * c)
	b = b + (b * d)
	anos = anos + 1
print(anos)