temp=float(input())
v=float(input())
if( temp>-50 and temp<10):
		if(v>(4.8)):				
			sens=13.12+0.6215*temp-(11.37*v**0.16)+(0.3965*temp*v**0.16)
			print(round(sens,4))
		else:
			print("Velocidade invalida")
else:
	print("Temperatura invalida")