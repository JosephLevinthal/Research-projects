x = (float(input( "digite um numero entre -100 e 100: " )))
t = - 1/x
p = 1/x
if(x < -100) and (x > 100) and (x == 0):
	print("entrada invalida")
elif(x >= -100) and (x < 0):
	print(round(t, 4))
elif(x > 0) and (x <= 100):
	print(round(p, 4))
else:
	print("entrada invalida")