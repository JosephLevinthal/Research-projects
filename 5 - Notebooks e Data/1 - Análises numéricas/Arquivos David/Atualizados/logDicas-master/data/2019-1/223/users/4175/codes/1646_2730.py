# Ao testar sua solução, não se limite ao caso de exemplo.
x = float(input()) 
y = float(input())

Q1 = x > 0 , y > 0
Q2 = x < 0 , y > 0
Q3 = x < 0 , y < 0
Q4 = x > 0 , y < 0

if (x>0) and (y>0) or (x<0) and (y>0):
	print("Superiores")
			
if (x<0) and (y<0) or (x>0) and (y<0):
	print("Inferiores")