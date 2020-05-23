# Ao testar sua solução, não se limite ao caso de exemplo.

x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))

if (x==y and y==0):
    print("Origem")
elif(x==0):
    print("Eixo X")
elif(y==0):
    print("Eixo Y")
elif(x>0)and(y>0):
    print("Q1")
elif(x<0)and(y>0):
    print("Q2")
elif(x<0) and (y<0):
    print("Q3")
elif(x>0)and(y<0):
    print("Q4")