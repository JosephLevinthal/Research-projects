x = float(input("digite o valor de x: "))
from math import*
if (x > -2):
      a = asin(x)
      b = acos(x)
      ars = degrees(a)
      arc = degrees(b)
else:
   if(x >= -1 and x < -0.5 or x > 0.5 and x <= 1):
		a = asin(x)
		ars = degrees(a)
	   print(round(ars, 2))
		
   elif(x >= -0.5 and x <= 0.5):
	   print(round(arc, 2))
		
   else:
	   print("entrada invalida")