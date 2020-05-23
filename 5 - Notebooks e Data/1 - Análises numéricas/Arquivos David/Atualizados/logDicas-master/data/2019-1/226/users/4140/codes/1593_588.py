saque=int(input());
#qunatidade de notas de 100
quantidade1=saque//100;

#quantidade de notas de 50
quantidade2=saque%100;
quantidade3=quantidade2//50;

#quantidade de notas de 10
quantidade4=saque%50;
quantidade5=quantidade4//10;

print(quantidade1)
print(quantidade3)
print(quantidade5)