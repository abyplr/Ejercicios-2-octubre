import math
a = 6378137.0
c = 6356752.314245
e2 = 1 - ((c ** 2) / (a ** 2))
S = 2 * math.pi * (a ** 2) * (1 + (((1 - e2) / (e2 ** (1/2))) * math.atanh (e2 ** (1/2))))
print("El área del elipsoide de referencia es: ", S, "m")

r = 6371000 
A = 4 * math.pi * (r ** 2)
print ("Y el área de la superficie de la Tierra suponiendi que se trata de una esfera es de: ", A, "m")

comparacion = ((S - A) / S) * 100
print("La diferencia es: ", comparacion)