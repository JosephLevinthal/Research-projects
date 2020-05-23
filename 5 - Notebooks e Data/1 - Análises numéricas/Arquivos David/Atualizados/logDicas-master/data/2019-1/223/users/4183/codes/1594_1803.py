x = int(input("Digite: "))
a = (x//1000)%10
b = (x//100)%10
c = (x//10)%10
d = (x//1)%10
cal = (d*2) + (c*3) + (b*4) + (a*5)
total = cal % 11
print(total)