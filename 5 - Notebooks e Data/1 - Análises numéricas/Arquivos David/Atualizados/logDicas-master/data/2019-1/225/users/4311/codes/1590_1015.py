a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
mi = min(a,b,c)
ma = max(a,b,c)
i = (a + b + c) - mi - ma
print(mi)
print(i)
print(ma)