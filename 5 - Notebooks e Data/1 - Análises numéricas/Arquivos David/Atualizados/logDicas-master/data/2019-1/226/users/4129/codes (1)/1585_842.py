num = int(input('Numero de quatro digitos:'))
#mil, cen, dez e uni representam unidade, dezena, centena e milhar
#Se dividirmos o primeio digito por 1000, teremos ele própri
#Ao subtrair o primeiro digito e dividir o valor inicial por 100, obtemos o terceiro digito
#A mesma ideia é acionada aqui, com intuito agora de conseguir o digito na casa dezenal
#Desse metodo se obtem todos os valores, por fim, soma-se
mil = num//1000
cen = (num-mil*1000)//100
dez = (num-(mil*1000)-(cen*100))//10
uni = (num-(mil*1000)-(cen*100)-(dez*10))//1
print(mil+cen+dez+uni)