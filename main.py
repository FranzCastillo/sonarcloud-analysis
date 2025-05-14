# main.py

import os
import sys
import math  # Importación no utilizada

def calcular_area_circulo(radio):
    if radio < 0:
        return None
    area = math.pi * radio ** 2
    return area

def obtener_nombre_usuario():
    nombre = input("Ingrese su nombre: ")
    if nombre == "":
        print("Nombre no proporcionado")
    else:
        print("Hola, " + nombre)
    return nombre

def procesar_datos(datos):
    resultado = []
    for i in range(len(datos)):
        if datos[i] % 2 == 0:
            resultado.append(datos[i] * 2)
        else:
            resultado.append(datos[i] + 1)
    return resultado

def main():
    radio = -5
    area = calcular_area_circulo(radio)
    print("Área del círculo:", area)

    nombre = obtener_nombre_usuario()

    datos = [1, 2, 3, 4, 5]
    resultado = procesar_datos(datos)
    print("Datos procesados:", resultado)

    # Código inalcanzable
    return
    print("Este mensaje nunca se mostrará")

main()
