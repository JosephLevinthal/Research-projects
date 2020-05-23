lado1=float(input());
lado2=float(input());
lado3=float(input());

s=(lado1+lado2+lado3)/2;
area=(s*(s-lado1)*(s-lado2)*(s-lado3))**0.5
print(round(area,5));
