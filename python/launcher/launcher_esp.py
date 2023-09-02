#IMPORTACIÓN MÓDULOS
import os
import time
import sys
import ctypes
import subprocess
import webbrowser

#LIMPIEZA PANTALLA
def limpiar_consola():
    if os.name == 'nt':#WINDOWS
        os.system('cls')
    else:#LINUX O MACOS
        os.system('clear')

#CAMBIO NOMBRE VENTANA
if sys.platform.startswith('win32'):#WINDOWS
    ctypes.windll.kernel32.SetConsoleTitleW("Lanzador de Servidores para Minecraft")
elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):#LINUX O MACOS
    sys.stdout.write(f"\x1b]2;Lanzador de Servidores para Minecraft\x07")

#BLOQUE REGRESO
def menu():
    return

#BLOQUE SELECCIÓN RAM INICIO
def ram():
    limpiar_consola()
    print("Lanzador de Servidores para Minecraft\n-------------------------------------\n\nPuedes volver al Menú Principal con 'N', o")
    while True:
        entrada = input("Ingresa los GB de RAM para asignar al Servidor= ")
        if entrada.lower() == 'n':
            break
        try:
            gbs = int(entrada)
            limpiar_consola()
            print("Lanzador de Servidores para Minecraft\n-------------------------------------\n")
            print("Iniciando el Server con",gbs,"GB de RAM")
            comando_java = f"java -Xmx{gbs}G -Xms{gbs}G -jar server.jar nogui"
            comando_final = str(comando_java)
            subprocess.run(comando_final, shell=True)
            input("\nPresiona una tecla para continuar")
            limpiar_consola()
            print("Lanzador de Servidores para Minecraft\n-------------------------------------\n\nServidor Cerrado\n\nPuedes revisar el registro en la carpeta 'logs'\n")
            input("Presiona una tecla para continuar")
            break
        except ValueError:
            ram()

#BLOQUE LICENCIAS
def about():
    limpiar_consola()
    url = "https://github.com/NGDPLNk/SSTools4MC/blob/main/LICENSE"
    print("Lanzador de Servidores para Minecraft\n-------------------------------------\n\nSe abrira la informacion sobre Licencia mas reciente en el navegador\n")
    print(url)
    print("")
    input("Presiona una tecla para continuar")
    webbrowser.open(url)

#BLOQUE SALIDA
def exiit():
    limpiar_consola()
    print("--------------------------------------------\nGracias por usar esta Herramienta\nMIT License - Copyright (c) 2023 NGDPL Nk\n--------------------------------------------\n")
    time.sleep(3)
    sys.exit()

#BLOQUE MENÚ PRINCIPAL
while True:
    limpiar_consola()
    print("Lanzador de Servidores para Minecraft\n-------------------------------------\n\nMenú Principal\n\n(1) Iniciar Servidor\n(2) Licencia\n(3) Salir\n")
    seleccion = input("Selecciona una opción= ")    
    if seleccion == "1":
        ram()
    elif seleccion == "2":
        about()
    elif seleccion == "3":
        exiit()
