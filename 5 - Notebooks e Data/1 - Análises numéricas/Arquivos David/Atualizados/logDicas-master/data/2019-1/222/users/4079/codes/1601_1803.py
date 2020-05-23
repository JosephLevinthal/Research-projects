nro = int(input("Digite um numero de 4 digitos:"))
milhar = nro // 1000
resto_milhar = nro % 1000
centena = resto_milhar // 100
resto_centena = resto_milhar % 100
dezena = resto_centena // 10
resto_dezena = resto_centena % 10
digito = int(((milhar * 5)+(centena*4)+(dezena*3)+(resto_dezena*2)) % 11)
print(digito)
