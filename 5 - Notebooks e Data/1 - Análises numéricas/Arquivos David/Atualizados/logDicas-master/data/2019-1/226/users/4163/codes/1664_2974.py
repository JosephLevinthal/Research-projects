a = int(input("quantidade de acai: "))
b = int(input("quantidade de salgados: "))
c = float(input("o valor pago: "))

k1= float(a*0.024)
s = float(3)



total =  k1 + b*s
if total < c:
	msg = "Sim" 
else:
	msg = "Nao"
	
print(round(total, 1))
print(msg)

