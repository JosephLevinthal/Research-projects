from numpy import*
v= array(eval(input("notas:")))
size(v)
media= (sum(v)-min(v))/(size(v)-1)
print(round(media,2))