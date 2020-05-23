from numpy import*
from numpy.linalg import*
vet = [[1,-1,0,0],[0,1,-1,0],[0,0,1,0],[1,0,0,1]]
vit = array([50,-120,350,870])
tot = dot(inv(vet),vit.T)
tot[0] = round(tot[0],1)
tot[1] = round(tot[1],1)
tot[2] = round(tot[2],1)
tot[3] = round(tot[3],1)
print(tot)