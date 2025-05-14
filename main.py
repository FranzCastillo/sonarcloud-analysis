# main.py

import os
import json
import sqlite3
import hashlib
import logging

# Configuración incorrecta del logging (nivel de DEBUG en producción)
logging.basicConfig(level=logging.DEBUG)

# Hardcoded credentials (problema de seguridad)
DB_PASSWORD = "1234"

# Función muy larga y compleja
def iniciar_aplicacion():
    logging.debug("Iniciando aplicación")
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    if usuario == "admin" and contrasena == "admin":  # credenciales quemadas
        print("Bienvenido admin")
    elif usuario == "":
        print("Nombre de usuario vacío")
    else:
        print("Usuario incorrecto")

    # SQL sin sanitizar (inyección de SQL posible)
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM usuarios WHERE nombre = '" + usuario + "';")
        resultado = cursor.fetchall()
        for row in resultado:
            print("Usuario:", row[0])
    except:
        print("Error al consultar la base de datos")
        pass

    # Código duplicado
    if usuario == "root":
        print("Root user")
    if usuario == "root":
        print("Root user")

    # Profundidad excesiva de anidamiento
    for i in range(5):
        for j in range(5):
            if i == j:
                if i + j > 3:
                    if i % 2 == 0:
                        if j % 2 == 1:
                            print(f"i:{i}, j:{j} - patrón especial")

    # Variable no utilizada
    datos_innecesarios = [1, 2, 3, 4]

    # Llamada insegura a eval (vulnerabilidad crítica)
    comando = input("Ingrese comando para eval: ")
    try:
        resultado = eval(comando)
        print("Resultado:", resultado)
    except Exception as e:
        print("Error al ejecutar eval:", e)

    # Archivos sin manejo adecuado de errores
    with open("usuarios.txt", "w") as f:
        f.write("usuario: " + usuario + "\n")

    # Uso de hash inseguro
    hash_contrasena = hashlib.md5(contrasena.encode()).hexdigest()
    print("Hash MD5 (inseguro):", hash_contrasena)

def funcion_mal_nombrada():
    a = 5
    b = 10
    c = 0
    for i in range(10):
        c = a * b + i
        print("Resultado:", c)

def repetir():
    repetir()
    # llamada recursiva sin condición de parada

iniciar_aplicacion()
