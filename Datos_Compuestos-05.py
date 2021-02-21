"""
5.- El tiempo como tuplas.
1. Proponer una representación con tuplas para representar el tiempo.
2. Escribir una función sumaTiempo que reciba dos tiempos dados y devuelva
su suma.
"""

tiempo1 = ("Horas", 1, "Minutos", 5,  "Segundos", 20)
tiempo2 = ("Horas", 0, "Minutos", 10,  "Segundos", 20)
print(tiempo1)
print(tiempo2)
h1 = tiempo1[1]
m1 = tiempo1[3] 
s1 = tiempo1[5]
h2 = tiempo2[1]
m2 = tiempo2[3] 
s2 = tiempo2[5]

def sumaTiempo(h1,h2,m1,m2,s1,s2):
    H3 = h1 + h2
    M3 = m1 + m2
    S3 = s1 + s2
    return H3, M3, S3
result = []
result = sumaTiempo(h1,h2,m1,m2,s1,s2)
print(result)
tiempo3 = "Horas: ", result[0], "Minutos: ", result[1],  "Segundos: ", result[2]
print(tiempo3)

