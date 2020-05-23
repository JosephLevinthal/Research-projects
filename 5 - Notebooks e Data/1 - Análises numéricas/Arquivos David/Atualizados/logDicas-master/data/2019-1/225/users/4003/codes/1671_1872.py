# Ao testar sua solução, não se limite ao caso de exemplo.


p = input().split()
x, y = p

x = float(x)
y = float(y)

if x == 0:
    elif y == 0:
      print('Origem')
   elif y != 0:
        print('Eixo Y')
if y == 0:
    elif x != 0:
      print('Eixo X')
if x > 0:
    if y > 0:
      print('Q1')
   if y < 0:
        print('Q4')
if x < 0:
    if y > 0:
      print('Q2')
   if y < 0:
        print('Q3')