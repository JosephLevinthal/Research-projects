from math import*
n= int(input(" digite um n "))
x1= n//1000
x2= n//100 - (n//1000)*10
x3= n//10 - (n//100)*10
x4= n//1 - (n//10)*10
final= (x1* 5)+(x2* 4)+(x3* 3)+(x4*2)
print(final %11)