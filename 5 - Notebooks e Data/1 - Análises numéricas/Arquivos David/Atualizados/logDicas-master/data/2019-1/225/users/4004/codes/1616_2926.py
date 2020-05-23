acai = int(input("quantidade de acai no copo: "))
esfirra = int(input("quantidade de esfirra: "))

Kg = acai / 1000
preco_acai = 24 * Kg
preco_esfirra = esfirra * 3
total = preco_acai + preco_esfirra

print(round(total, 2))