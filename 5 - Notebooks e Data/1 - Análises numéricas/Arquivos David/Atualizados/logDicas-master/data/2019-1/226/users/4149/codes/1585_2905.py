from math import sqrt
tri=float(input("medida do lado a:  "))
tri2=float(input("medida do lado b: "))
tri3=float(input("medida do lado c: "))

semi=(tri+tri2+tri3)/2

area=sqrt(semi*(semi-tri)*(semi-tri2)*(semi-tri3))

print(round(area,5))

