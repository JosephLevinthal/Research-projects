acai = int(input('Quantidade de acai em gramas:'))
esfirra = int(input('Quantidade de esfirra:'))
acaikg = acai/1000
esfirrapreco = 3*esfirra
acaipreco = acaikg*24
total = esfirrapreco+acaipreco

print(round(total, 2))