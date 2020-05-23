a = int(input("a:"))

a1 = a//1000
a2 = (a//100)%10
a3 = (a//10)%10
a4 = (a%10)

w = a1*5
x = a2*4
y = a3*3
z = a4*2

var = (w+x+y+z)%11
print(var)
