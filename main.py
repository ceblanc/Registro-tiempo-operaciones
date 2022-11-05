# Programa para registrar operaciones de reposicion de productos por usuario, proveedor y tiempo empleado.
# Una vez registrados, los datos se almacenan en un archivo csv

# Importacion de librerias

import csv
from datetime import datetime

# Creacion de listas para utilizar el programa. Mejorar utilizando un importador de usuarios y proveedores

lista_usuarios = ["Carlos", "Nacho", "Jara"]
lista_proveedores = ["Granero", "Horno de Adobe", "Natursoy"]

# Lista donde se almacenan los datos que seran guardados en formato csv

datos = []

# Creacion de los metodos

def comenzar():

    introduce_usuario()
    introduce_proveedor()
    introduce_reposicion()
    tiempo_de_operacion()

    print(datos)


def introduce_usuario():

    registro_usuario = input("Introduce tu usuario: ")

    if registro_usuario in lista_usuarios:
        print("Te has identificado como",registro_usuario)

        datos.append(registro_usuario)

    else:
        print("Usuario incorrecto")
        introduce_usuario()


def introduce_proveedor():
    registro_proveedor = input("Introduce el proveedor: ")

    if registro_proveedor in lista_proveedores:
        print("El proveedor seleccionado es", registro_proveedor)

        datos.append(registro_proveedor)

    else:
        print("Proveedor incorrecto")
        introduce_proveedor()


def introduce_reposicion():
    registro_reposicion = input("Introduce el tipo de reposición: 1. balda / 2. lineal ")

    if registro_reposicion == "balda":
        print("Has seleccionado Balda")

        datos.append(registro_reposicion)

    elif registro_reposicion == "lineal":
        print("Has seleccionado Lineal")

        datos.append(registro_reposicion)

    else:
        introduce_reposicion()

def ano():

    global hora_inicio_ano

    hora_inicio_ano = int(input("Introduce el año de inicio: "))

    if hora_inicio_ano == 2022:

        pass

    else:

        ano()

def mes():

    global hora_inicio_mes

    hora_inicio_mes = int(input("Introduce el mes de inicio: "))

    if hora_inicio_mes > 0 and hora_inicio_mes < 13:

        pass

    else:

        mes()

def dia():

    global hora_inicio_dia

    hora_inicio_dia = int(input("Introduce el dia de inicio: "))

    if hora_inicio_dia > 0 and hora_inicio_dia < 32:

        pass

    else:

        dia()

def hora():

    global hora_inicio_hora

    hora_inicio_hora = int(input("Introduce la hora de inicio: "))

    if hora_inicio_hora > 0 and hora_inicio_hora < 25:

        pass

    else:

        hora()

def minuto():

    global hora_inicio_minuto

    hora_inicio_minuto = int(input("Introduce el minuto de inicio: "))

    if hora_inicio_minuto >= 0 and hora_inicio_minuto < 61:

        pass

    else:

        minuto()

def tiempo_de_operacion(): #Modificar: Una funcion por cada variable para volver a solicitar si ocurre un error

    ano()

    mes()

    dia()

    hora()

    minuto()

    hora_inicio = datetime(hora_inicio_ano, hora_inicio_mes, hora_inicio_dia, hora_inicio_hora, hora_inicio_minuto)
    print("Has iniciado la operacion en", hora_inicio)

    hora_fin = datetime.now()  # Se registra la operacion en el momento de finalizarla

    # Calculo del tiempo empleado en la operacion

    diferencia = hora_fin - hora_inicio
    minutos_brutos = diferencia.total_seconds() / 60
    minutos_operacion = round(minutos_brutos, 0)
    datos.append(minutos_operacion)


def exportar_csv():
    archivo = open("operaciones.csv", "a", newline='')
    reader = csv.writer(archivo)
    reader.writerow(datos)
    archivo.close()

# Inicio del programa

if __name__ == "__main__":
    comenzar()
    exportar_csv()
