from numpy import*
v= array(eval(input("vetor:")))
media= (((v[0]**1/6+v[1]**1/6+v[2]**1/6+v[3]**1/6)/size(v))**6)
print(round(media,2))