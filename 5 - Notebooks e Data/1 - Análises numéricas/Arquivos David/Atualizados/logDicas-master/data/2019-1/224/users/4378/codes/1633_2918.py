a=float(input("valor do ingresso: "))
b=int(input("quantidade de ingressos: "))
tot=a*b
promo=a-(a*(20/100))
vp=tot-promo
print(round(vp, 2))