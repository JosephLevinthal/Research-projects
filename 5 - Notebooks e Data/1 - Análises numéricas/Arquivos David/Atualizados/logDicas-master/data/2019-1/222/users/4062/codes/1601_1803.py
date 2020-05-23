valor=int(input("Digite um numero de 4 digitos"))
a=valor//1000
b=(valor-(a*1000))//100
c=(valor-(a*1000)-(b*100))//10
d=(valor-(a*1000)-(b*100)-(c*10))

digver=(d*2+c*3+b*4+a*5)%11
print(digver)