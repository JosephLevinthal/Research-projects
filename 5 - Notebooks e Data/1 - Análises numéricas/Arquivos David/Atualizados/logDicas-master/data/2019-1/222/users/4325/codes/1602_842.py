number = int(input("Digite um numero com quatro digitos:"))
num1 = (number//1000)
num2 = (number//100)%10
num3 = (number//10)%10
num4 = (number%10)
soma = (num1+num2+num3+num4)
print (soma)