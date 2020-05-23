digitos = int(input('Insira quatro digitos:'))
d1 = digitos%10
d2 = (digitos%100)//10
d3 = (digitos%1000)//100
d4 = (digitos%10000)//1000
multi = (d1*2)+(d2*3)+(d3*4)+(d4*5)
verif = multi%11


print(verif)