x = int(input("digite um numero: "))
y = x//1000
z = (x //100)-(x// 1000*10)
w = x // 10 - (x // 100) * 10
r = x - (x//10)*10
var1 = ((y * 5) + (z * 4) + (w * 3) + (r * 2)) % 11
print(var1)