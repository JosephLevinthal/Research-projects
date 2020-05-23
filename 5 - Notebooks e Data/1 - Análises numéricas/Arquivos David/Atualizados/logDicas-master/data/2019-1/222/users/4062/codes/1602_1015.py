a1 = int(input("valor de a: "))
b1 = int(input("valor de b: "))
c1 = int(input("valor de c: "))
mini = min(a1,b1,c1)
maxi = max(a1,b1,c1)
media = a1 + b1 + c1 - maxi - mini
print(mini)
print(media)
print(maxi)