#IMPORTACIÓN DE MÓDULOS
import os
import sys
import ctypes
import subprocess

#LIMPIEZA DE PANTALLA
def limpiar_consola():
    if os.name == 'nt':  #WINDOWS
        os.system('cls')
    else:  #LINUX O MACOS
        os.system('clear')

#CAMBIO DE NOMBRE DE VENTANA
if sys.platform.startswith('win32'):  #WINDOWS
    ctypes.windll.kernel32.SetConsoleTitleW("Lanzador de Servidores para Minecraft")
elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):  #LINUX O MACOS
    sys.stdout.write(f"\x1b]2;Lanzador de Servidores para Minecraft\x07")

def starting():
    limpiar_consola()
    print("Lanzador de Servidores para Minecraft")
    print("-------------------------------------")
    print("")
    print("Iniciando el Server con " + gbs + "GB de RAM")
    comando_java = "java -Xmx" + gbs + " -Xms" + gbs + " -jar server.jar nogui"
    resultado = subprocess.run(comando_java, shell=True, capture_output=True, text=True)
    print(resultado.stdout)
    input()

#BLOQUE DE SELECCIÓN DE RAM
def ram():
    limpiar_consola()
    print("Lanzador de Servidores para Minecraft")
    print("-------------------------------------")
    print("")
    print("Puedes volver al Menú Principal con 'N', o")
    while True:
        try:
            gbs = int(input("Ingresa los GB de RAM para asignar al Servidor= "))
            starting()
        except ValueError:
            ram()

def about():
    limpiar_consola()
    #CÓDIGO AQUÍ

def exiit():
    limpiar_consola()
    #CÓDIGO AQUÍ

def dbmode():
    limpiar_consola()
    #CÓDIGO AQUÍ

while True:
    limpiar_consola()
    print("Lanzador de Servidores para Minecraft")
    print("-------------------------------------")
    print("")
    print("Menú Principal")
    print("")
    print("(1) Iniciar Servidor")
    print("(2) Licencia")
    print("(3) Salir")
    print("")
    
    seleccion = input("Selecciona una opción= ")
    
    if seleccion == "1":
        ram()
    elif seleccion == "2":
        about()
    elif seleccion == "3":
        exiit()
    elif seleccion == "4":
        dbmode()

input()
