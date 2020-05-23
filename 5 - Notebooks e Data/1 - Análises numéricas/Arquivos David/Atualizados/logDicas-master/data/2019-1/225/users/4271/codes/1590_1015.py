num1 = int(input("digite numero 1: "))
num2 = int(input("digite numero 2: ")) 
num3 = int(input("digite numero 3: "))

Interm = num1 + num2 + num3 - min(num1, num2, num3) - max(num1, num2, num3)

print(min(num1, num2, num3))
print(interm)
print(max(num1, num2, num3))
