a = int(input("v"))
b = (a//1000)*10
c = (a//100)*10
d = (a//10)*10
e = (a//1)*10
r = ((a*2)+(b*3)+(c*4)+(d*5))%11
print(r)