senha = int(input("digite uma senha de 4 digitos: "))
d1 = senha // 1000
d2 = (senha % 1000) // 100
d3 = ((senha % 1000) % 100) // 10
d4 = ((senha % 1000)% 100) % 10
d1 = d1 * 5
d2 = d2 * 4
d3 = d3 * 3
d4 = d4 * 2
somatorio = (d1 + d2 + d3 + d4) % 11
print(somatorio)