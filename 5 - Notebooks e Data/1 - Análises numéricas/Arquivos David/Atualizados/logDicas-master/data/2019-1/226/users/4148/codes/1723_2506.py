q = int(input("quant.: "))
pc = int(input("percentual: "))
qvc = int(input("quant. de venda: "))

ano  = 0
cap = 12000

while(q>0 and q<cap):
	q = q + (q*(pc/100))-qvc
	ano = ano +1

if (q<0):
	print("EXTINCAO")
if(q>cap):
	print("LIMITE")

print(ano)

		