#!/usr/bin/env python

"""
Consigna:Crea una lista vacÃƒÂ­a (pongamos 10 posiciones), pide sus valores
y devuelve la suma, el promedio y la desviacion estandar de los nÃƒÂºmeros.
Imprime la lista de numeros.
"""
lista=[]
suma=0
prom=0
num=0
for i in range(10):
    num = int(input("Ingrese un nÃºmero: "))
    lista.append(num)
    suma += num
for i in lista:
    print(i)

prom = suma / len(lista)

print("La suma es ",suma)
print("El promedio es ",prom)
