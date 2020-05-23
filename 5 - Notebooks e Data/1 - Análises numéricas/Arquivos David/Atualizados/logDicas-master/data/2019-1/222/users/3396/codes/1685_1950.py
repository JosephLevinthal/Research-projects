tar = float(input("temperatura do ar: "))
v = float(input("velocidade do vento: "))
t = 13.12+0.6215*tar-(11.37*v**0.16)+(0.3965*tar*v**0.16)
if(tar>=-50 and tar<=10 and v>4.8):
    print(round(t,4))
elif(tar<-50 or tar>=10):
    print("Temperatura invalida")
else:
    print("Velocidade invalida")