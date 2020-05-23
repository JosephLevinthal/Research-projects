x1= int(input("qual seu numero 1? "))
x2= int(input("qual seu numero 2? "))
x3= int(input("qual seu numero 3? "))
if (x1<x2<x3):
	print(x2)
if(x2<x1<x3):
	print(x1)
if(x1<x3<x2):
	print(x3)
if(x3<x1<x2):
	print(x1)
if(x2<x3<x1):
	print(x3)
if(x3<x2<x1):
	print(x2)