from numpy import*
vector = array(eval(input("medias: ")))

i = 0
med = 1
while(i<size(vector)):
	med = med * vector[i]
	i = i + 1
media = (med)**(1/size(vector))
print(round(media,2))