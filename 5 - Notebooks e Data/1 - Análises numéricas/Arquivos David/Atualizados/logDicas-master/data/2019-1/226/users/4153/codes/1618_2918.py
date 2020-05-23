pvii = float(input("Insira o preco do valor integral do ingresso: "))  #pvii = valor do igresso
qi = int(input("Insira a quantidade de ingressos: "))                  #qi = quantidade de ingrgessos

promocao = pvii * (20 / 100)                          # promocao de 20%
precoPromocional = pvii - promocao                    # preco promocional 
vtc = precoPromocional * qi                           # valor total da compra

print(round(vtc, 2))