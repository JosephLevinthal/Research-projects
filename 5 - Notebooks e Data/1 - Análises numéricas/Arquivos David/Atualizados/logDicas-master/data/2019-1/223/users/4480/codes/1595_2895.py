q = float(input("qual a quantidade de jogos? "))
vu = float(input("qual o valor unitario do jogo? "))
frete = float(input(" qual o frete? "))
total = q * vu + frete
print(round(total, 2))