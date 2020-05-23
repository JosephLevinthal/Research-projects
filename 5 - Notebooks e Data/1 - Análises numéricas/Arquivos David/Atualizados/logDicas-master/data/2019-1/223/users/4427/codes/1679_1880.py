# Ao testar sua solução, não se limite ao caso de exemplo.
mes = int(input())

jan = "janeiro"
fev = "fevereiro"
mar = "marco"
abr = "abril"
mai = "maio"
jun = "junho"
jul = "julho"
ago = "agosto"
set = "setembto"
out = "outubro"
nov = "novembro"
dez = "Dezembro"

if mes <=12 and mes >= 1:
    if mes == 1:
        print(jan)
    if mes == 2:
        print(fev)
    if mes == 3:
        print(mar)
    if mes == 4:
        print(abr)
    if mes == 5:
        print(mai)
    if mes == 6:
        print(jun)
    if mes == 7:
        print(jul)
    if mes == 8:
        print(ago)
    if mes == 9:
        print(set)
    if mes == 10:
        print(out)
    if mes == 11:
        print(nov)
    if mes == 12:
        print(dez)
else:
    print("numero de mes invalido")