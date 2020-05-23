from numpy import*
vetnot = array(eval(input("notas: ")))

media = (sum(vetnot) - min(vetnot))/(size(vetnot) - 1)

print(round(media,2))