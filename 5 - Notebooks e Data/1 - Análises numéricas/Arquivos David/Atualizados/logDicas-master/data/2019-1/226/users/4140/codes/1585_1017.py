from math import *
latitude1=radians(float(input()));
longitude1=radians(float(input()));
latitude2=radians(float(input()));
longitude2=radians(float(input()));

d= 6371.01*acos(sin(latitude1)*sin(latitude2)+ cos(latitude1)* cos(latitude2)*cos(longitude1-longitude2));
print(round(d,2))