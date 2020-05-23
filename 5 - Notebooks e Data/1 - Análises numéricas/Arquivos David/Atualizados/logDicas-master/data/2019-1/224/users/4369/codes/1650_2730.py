# Ao testar sua solução, não se limite ao caso de exemplo.
x = float(input("Digite x: "))
y = float(input("Digite y: "))

if(x > 0 and y > 0):
	print("Superiores")
elif(x < 0 and y > 0):
	print("Superiores")
elif(x > 0 and y < 0):
	print("Inferiores")
else:
	print("Inferiores")