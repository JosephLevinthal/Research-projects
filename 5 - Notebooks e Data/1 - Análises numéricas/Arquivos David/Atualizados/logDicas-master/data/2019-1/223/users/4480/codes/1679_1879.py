# Ao testar sua solução, não se limite ao caso de exemplo.
hextras = float(input(""))
hfalta = float(input(""))

print(hextras, "extras", "e", hfalta, "de falta")
H = (hextras)- 1/4 *(hfalta)
if(H>400):
	g = 500.00
else:
	g = 100.00
print("R$", round(g,2))