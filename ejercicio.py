#!/usr/bin/env python

"""
Consigna:Crea una lista vacÃƒÂ­a (pongamos 10 posiciones), pide sus valores
y devuelve la suma, el promedio y la desviacion estandar de los nÃƒÂºmeros.
Imprime la lista de numeros.
"""
import math

def desviacion_estandar(valores,media):
    suma = 0
    for valor in valores:
        suma += (valor - media) ** 2

    radicando = suma / (len(valores))

    return math.sqrt(radicando)

lista=[]
suma=0
prom=0
num=0
for i in range(10):
    num = int(input("Ingrese un numero: "))
    lista.append(num)
    suma += num
for i in lista:
    print(i)

prom = suma / len(lista)

dev_std = desviacion_estandar(lista, prom)

print("La suma es: ",suma)
print("El promedio es: ",prom)
print("La desviación estándar es: ",dev_std)

