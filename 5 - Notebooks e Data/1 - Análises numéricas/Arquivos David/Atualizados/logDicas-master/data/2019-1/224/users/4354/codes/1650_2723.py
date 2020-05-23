num1 = float(input("primeiro numero: "))
num2 = float(input("segundo numero: "))
num3 = float(input("terceiro numero: "))

if(num1 < num2 < num3) :
	print(num3)
if(num2<num1<num3) :
	print(num3)
if(num1<num3<num2) :
	print(num2)
if(num3< num2 <num1) :
	print(num1)
if(num3<num1<num2) :
	print(num2)
if(num2<num3<num1) :
	print(num1)