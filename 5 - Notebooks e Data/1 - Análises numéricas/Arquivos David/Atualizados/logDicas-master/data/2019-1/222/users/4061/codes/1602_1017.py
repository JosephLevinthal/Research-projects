# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
import math

lat1 = math.radians(float(input("Latitude de P1: ")))
long1 = math.radians(float(input("longitude de P1: ")))
#---------------------------------------------
lat2 = math.radians(float(input("Latitude de P2: ")))
long2 = math.radians(float(input("longitude de P2: ")))

r = float(6371.01)

angulo = r*(math.acos((math.sin(lat1)*math.sin(lat2))+(math.cos(lat1)*math.cos(lat2)*math.cos(long1-long2))))
print(round(angulo,2))