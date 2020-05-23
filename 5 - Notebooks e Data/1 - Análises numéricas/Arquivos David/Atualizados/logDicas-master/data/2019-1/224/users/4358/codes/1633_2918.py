precoingresso=(float(input("Qual o valor integrau do ingresso ?")))
quantidadeingresso=(int(input("Qual a quantidade de ingressos?")))
valortotaldacompra=precoingresso*quantidadeingresso
print(round(valortotaldacompra, 2))
precoPromocional= precoingresso-(precoingresso*(20/100))
print(round(precoPromocional, 2))