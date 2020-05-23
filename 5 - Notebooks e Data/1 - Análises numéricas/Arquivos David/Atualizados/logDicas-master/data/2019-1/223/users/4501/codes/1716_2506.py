a=int(input("quantidade: "))
b=int(input("crescimento: "))
c=int(input("retirada: "))
anos=0
while(0 < a < 12000):
	acres = a * b/100
	a = a + acres
	a = a - c
	anos = anos + 1
if(a <= 0):
	print("EXTINCAO")
else:
	print("LIMITE")
print(anos)	