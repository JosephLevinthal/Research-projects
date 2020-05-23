#primeiramente importamos o valor de pi do math
from math import *
#definimos as variaveis da equacao
R=float(input("distancia do cento da rosquinha para seu tubo em cm"))
r=float(input("grossura da rsoquinha em cm"))
Q=float(input("quantidade de rosquinhas que se quer fazer"))
M=(2*pi**2)*R*(r**2)*Q
m=round(M, 2)
print(m)
