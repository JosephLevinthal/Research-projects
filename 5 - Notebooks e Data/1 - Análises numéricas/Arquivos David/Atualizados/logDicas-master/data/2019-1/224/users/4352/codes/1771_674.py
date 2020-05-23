from numpy import*
v = array(eval(input("digite seu vetor: ")))
quantv = size(v)
maior = max(v)
menor = min(v)
soma = sum(v)
media = soma/quantv
print(quantv)
print(v[0])
print(v[4])
print(maior)
print(menor)
print(soma)
print(round(media, 2))