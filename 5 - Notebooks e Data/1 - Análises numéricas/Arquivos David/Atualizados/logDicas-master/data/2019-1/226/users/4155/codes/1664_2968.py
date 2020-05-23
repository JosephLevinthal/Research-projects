x = input("lanche: ").upper()
q = int(input("quantidade: ")) 
r = int(input("refrigerante: ")) 
x = "L"

if(x != "L"):
	msg = (q * 3.50) + (r * 4.00)
else:
	msg = (q * 5.00) + (r * 4.00)
	
r = round(msg, 2)
print(r)