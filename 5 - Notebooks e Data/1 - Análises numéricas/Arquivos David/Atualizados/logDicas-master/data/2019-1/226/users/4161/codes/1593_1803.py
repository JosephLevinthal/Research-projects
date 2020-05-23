n = int(input("digite o numero: "))
w = n//1000 
x = n//100 - w*10
y = n//10 - (n//100)*10
z = n - (n//10)*10

c1 = w*5
c2 = x*4
c3 = y*3
c4 = z*2
s = c1 + c2 + c3 + c4
r = s % 11
print(r)