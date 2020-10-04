#!/usr/bin/env python

"""
Consigna:Crea una lista vacÃ­a (pongamos 10 posiciones), pide sus valores
y devuelve la suma, el promedio y la desviacion estandar de los nÃºmeros.
Imprime la lista de numeros.
"""
lista=[]

suma=0
prom=0
num=0
for i in range(10):
    num = int(input("Ingrese un número: "))
    lista.append(num)
    suma += num
for i in lista:
    print(i)

media = suma / len(lista)

print("La suma es ",suma)
print("El promedio es ",promedio)