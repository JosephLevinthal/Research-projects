a = int(input("Digite a hab a: "))
b = int(input("Digite a hab b: "))
cresca = float(input("Digite a hab pa: "))
crescb= float(input("Digite a hab pb: "))

cresca = cresca/100
crescb = crescb/100

anos =0
while(a<b):
	a = a + a*cresca
	b =  b + b *crescb
	anos = anos + 1
	
print(anos)
	