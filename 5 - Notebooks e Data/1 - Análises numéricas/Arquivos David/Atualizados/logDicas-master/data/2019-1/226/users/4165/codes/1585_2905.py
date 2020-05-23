lado1 = float(input( "valor do lado"))
lado2 = float(input( "valor do lado"))
lado3 = float(input( "valor do lado"))
semi = (lado1 + lado2 + lado3)/2
from math import *
areap = sqrt(semi*(semi - lado1)*(semi - lado2)*(semi - lado3))
print(round(areap,5))