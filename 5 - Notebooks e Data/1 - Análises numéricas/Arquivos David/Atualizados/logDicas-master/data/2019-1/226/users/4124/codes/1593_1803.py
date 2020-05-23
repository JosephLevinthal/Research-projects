num = int(input("Digite um numero de quatro digitos: "))

num1 = num // 1000
num1a = num % 1000
num2 = num1a // 100
num2a = num1a % 100
num3 = num2a // 10
num3a = num2a % 10
num4 = num3a

soma = (num1 * 5 + num2 * 4 + num3 * 3 + num4 * 2)
print(soma % 11)