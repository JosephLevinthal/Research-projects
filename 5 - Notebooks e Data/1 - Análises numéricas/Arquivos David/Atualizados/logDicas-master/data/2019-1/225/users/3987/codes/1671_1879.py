# Ao testar sua solução, não se limite ao caso de exemplo.
n = float(input("e:"))
no = float(input("f:"))

print(n,"extras e", no,"de falta")
h = n - ((1//4) * no)
if(400.00 < h):
	r = 500.00
else:
	r = 100.00
print("R$",round(r,2))
