from math import *
var1=int(input("pontos de vida iniciais:"))
var2=int(input("D1:"))
var3=int(input("D2:"))
x=(pi)**(var3//3)
y=(5*var2)**(1/2)
dano=(x+y)
vidafinal=(var1-dano)
print(int(vidafinal))