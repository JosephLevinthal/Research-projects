pa = int(input())
pb = int(input())
g1 = float(input())
g2 = float(input())

cont = 0

while pa <= pb:
    pa = (pa +((pa * g1) / 100))
    pb = (pb +((pb * g2) / 100))
    cont = cont +1

print (cont)