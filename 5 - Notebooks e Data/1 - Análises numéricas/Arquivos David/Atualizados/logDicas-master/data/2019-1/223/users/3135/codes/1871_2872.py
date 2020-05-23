from numpy import*
from numpy.linalg import*

m= array(eval(input("Insira sua entrada:")))
area= m.shape[1]


for i in range(size(m)):	
	area= (m[:,0]* m[:,1])/2	
	
a=sum(area)
media=a/m.shape[0]
print(round(media,2))


