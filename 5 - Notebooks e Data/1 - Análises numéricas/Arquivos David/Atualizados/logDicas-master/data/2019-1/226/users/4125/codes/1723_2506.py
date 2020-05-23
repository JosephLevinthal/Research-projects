t = int(input("tambaqui: "))
p1 = float(input("percentual: "))/100
t1 = int(input("quantidade retirada: "))
anos = 0
while(t>0)and(t<12000):
	t = t + p1*t - t1
	anos = anos + 1
if(t<=0):
	print("EXTINCAO")
	print(anos)
elif(t >=12000):
	print("LIMITE")
	print(anos)