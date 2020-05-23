x = float(input("preco sem desconto:"))

if(x >= 200):
	msg = (x * 95) / 100
else:
	msg = x
	
r = round(msg, 2)

print(r)