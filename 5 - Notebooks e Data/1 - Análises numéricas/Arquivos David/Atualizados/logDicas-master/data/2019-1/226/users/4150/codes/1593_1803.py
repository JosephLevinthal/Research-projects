num = int(input("digite: "))

a = (num//1000)

b = (num%1000)
b1 = (b//100)

c = (num//10)
c1 = (c % 10)

d = (num%1000)
d1 = (d % 10 )

codv = ((a*5)+(b1*4)+(c1*3)+(d1*2))%11

print(int(codv))