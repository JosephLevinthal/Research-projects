# Ao testar sua solução, não se limite ao caso de exemplo.
x = float(input("Insira um valor: "))
y = float(input("Insira um valor: "))
if ((x>0 and y>0) or (x<0 and y>0)):
	print("Superiores")
else:
	print("Inferiores")