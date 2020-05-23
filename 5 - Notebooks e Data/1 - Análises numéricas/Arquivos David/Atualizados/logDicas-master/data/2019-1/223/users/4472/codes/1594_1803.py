numero = int(input("Conta: "))

#isolar numeros
num1 = numero // 1000
num2 = numero // 100 % 10
num3 = numero // 10 % 10
num4 = numero % 10

#contar numeros
cont1 = num4 * 2
cont2 = num3 * 3
cont3 = num2 * 4
cont4 = num1 * 5

#somar e dividir por 11
digito = (cont1 + cont2 + cont3 + cont4) % 11

print (digito)