#primeiros colocamos a variavel do numero
numero=int(input("numero"))
#separo o primeiro digito
pdigito=numero//1000
resto1=numero%1000
#separo o segundo digito
sdigito=resto1//100
resto2=resto1%100
#separo o terceiro digito
tdigito=resto2//10
resto3=resto2%10     #nota=se que o resto3 e o qdigito
#defino o print da soma
soma=pdigito+sdigito+tdigito+resto3
print(soma)
