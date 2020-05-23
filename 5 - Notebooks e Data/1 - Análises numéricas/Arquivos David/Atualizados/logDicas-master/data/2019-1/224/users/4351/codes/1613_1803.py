conta= int(input("numero de quatro digitos"))
d1= conta//1000
resto1=conta%1000
d2= resto1//100
resto2= resto1%100
d3= resto2//10
d4=resto2%10
verificador= ((d1*5)+(d2*4)+(d3*3)+(d4*2))%11
print(verificador)
