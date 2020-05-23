# Ao testar sua solução, não se limite ao caso de exemplo.
x=float(input("x"))
y=float(input("y"))
if( (x>0) , (y>0) ):
	print("Superiores")

if( (x<0) , (y>0) ):
	print("Superiores")

if( (x<0) , (y<0) ):
	print("Inferiores")

if( (x>0) , (y<0) ):
	print("Inferiores")
