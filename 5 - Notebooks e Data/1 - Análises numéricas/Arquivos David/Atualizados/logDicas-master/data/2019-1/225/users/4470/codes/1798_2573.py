from numpy import*
peso = array(eval(input("pesos:")))
altura = array(eval(input("altura:")))

imc = zeros(size(peso), dtype = float)
i = 0
while( i < size(peso)):
    imc[i] = round((peso[i])/(altura[i] * altura[i]),2)
    i = i + 1
print(imc)

sit = " "
i = max(imc)

if(i<17):
    sit = "muito abaixo do pesoa"
elif(17<=i<=18.49):
    sit = "abaixo do peso"
elif(18.5<=i<=24.99):
    sit = "peso normal"
elif(25<=i<=29.99):
    sit = "acima do peso"
elif(30<=i<=34.99):
    sit = "obesidade"
elif(35<=i<=39.99):
    sit = "obesidade severa"
elif(i>40):
    sit = "obesidade morbida"
else:
    sit = "dados invalidos"
print("O MAIOR IMC DA TURMA EH:", max(imc))
print(sit.upper())