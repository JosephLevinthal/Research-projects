num = int(input("Digite aqui um numero inteiro de quatros digitos: "))

var1 = int(num % 10) * 2

var2 = int((num % 100) // 10) * 3

var3 = int((num % 1000) // 100) * 4

var4 = int(num // 1000) * 5

soma = var1 + var2 + var3 + var4

digito = int(soma % 11)

print(digito)