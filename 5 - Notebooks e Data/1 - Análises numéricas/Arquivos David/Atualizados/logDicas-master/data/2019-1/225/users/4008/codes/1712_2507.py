qip =  int(input("quantidade inicial de pirarucus: "))
pc =  int(input("percentual de crescimento: "))
t= 0
while(qip < 8000 and qip>0):
	qv= int(input("rettirados para venda: "))
	qip = qip + ((qip * pc)/100) - qv
	t = t+1
if(qip >8000):
	print("MAXIMO")
else:
	print("ZERO")
print(t)