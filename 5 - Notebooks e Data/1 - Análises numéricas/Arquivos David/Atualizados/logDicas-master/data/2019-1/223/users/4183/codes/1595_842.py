dig = int(input("digito"))
a = (dig//1000)%10
b = (dig//100)%10
c = (dig//10)%10
d = (dig//1)%10
total = a+b+c+d
print(total)