jogo1 = float(input('valor 1'))
jogo2 = float(input('valor 2'))
desconto = 25
TotalJogo2 = jogo2 - (jogo2*(desconto/100))
total = (jogo1 + TotalJogo2)
print(round(TotalJogo2,2))
print(round(total,2))