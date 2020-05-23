from math import *
t1 = radians(float(input("digite a latitude: ")))
g1 = radians(float(input("digite a longitude: ")))
t2 = radians(float(input("digite a latitude: ")))
g2 = radians(float(input("digite a longitude: ")))

R = 6371.01

sen_t1 = sin(t1)
sen_t2 = sin(t2)
cos_t1 = cos(t1)
cos_t2 = cos(t2)

sub_t1t2 = g1 - g2

cos_sub = cos(sub_t1t2)

d = R * (acos((sen_t1 * sen_t2) + cos_t1 * cos_t2 * cos_sub))

print(round(d,2))