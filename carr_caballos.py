import time
import random
import os
from xml.etree.ElementTree import C14NWriterTarget


class caballo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.posicion = 0

    def mover(self):
        self.posicion += random.randint(0, 1)


c1 = caballo("Juan")
c2 = caballo("Speedy")
c3 = caballo("Mike Tyson")
c4 = caballo("Estorbo")
c5 = caballo("Lentín")

def jugar():
    while True:

        print(" ██████╗ █████╗ ██████╗ ██████╗ ███████╗██████╗  █████╗     ██████╗ ███████╗     ██████╗ █████╗ ██████╗  █████╗ ██╗     ██╗      ██████╗ ███████╗",
            "\n██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗    ██╔══██╗██╔════╝    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██║     ██║     ██╔═══██╗██╔════╝",
            "\n██║     ███████║██████╔╝██████╔╝█████╗  ██████╔╝███████║    ██║  ██║█████╗      ██║     ███████║██████╔╝███████║██║     ██║     ██║   ██║███████╗",
            "\n██║     ██╔══██║██╔══██╗██╔══██╗██╔══╝  ██╔══██╗██╔══██║    ██║  ██║██╔══╝      ██║     ██╔══██║██╔══██╗██╔══██║██║     ██║     ██║   ██║╚════██║",
            "\n╚██████╗██║  ██║██║  ██║██║  ██║███████╗██║  ██║██║  ██║    ██████╔╝███████╗    ╚██████╗██║  ██║██████╔╝██║  ██║███████╗███████╗╚██████╔╝███████║",
            "\n ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚══════╝     ╚═════╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝"
        )
        print("\n\n\n")
        print('\x1b[1;30;47m' + ' Juan  <><><><><><><><><><><><><><><> ' + '\x1b[0m')
        for x in range(c1.posicion):
            print(" ", end="")
        print("🐎")

        print('\x1b[1;30;47m' + ' Speedy  <><><><><><><><><><><><><><> ' + '\x1b[0m')
        for x in range(c2.posicion):
            print(" ", end="")
        print("🐎")

        print('\x1b[1;30;47m' + ' Mike Tyson  <><><><><><><><><><><><> ' + '\x1b[0m')
        for x in range(c3.posicion):
            print(" ", end="")
        print("🐎")

        print('\x1b[1;30;47m' + ' Estorbo  <><><><><><><><><><><><><>< ' + '\x1b[0m')
        for x in range(c4.posicion):
            print(" ", end="")
        print("🐎")

        print('\x1b[1;30;47m' + ' Lentín  <><><><><><><><><><><><><><> ' + '\x1b[0m')
        for x in range(c5.posicion):
            print(" ", end="")
        print("🐎")

        c1.mover()
        c2.mover()
        c3.mover()
        c4.mover()
        c5.mover()

        if c1.posicion >= 38 or c2.posicion >= 38 or c3.posicion >= 38 or c4.posicion >= 38 or c5.posicion >= 38:
            if c1.posicion >= 38:
                print("Gana Juan!")
                return c1.nombre  
            if c2.posicion >= 38:
                print("Gana Speedy!")
                return c2.nombre
            if c3.posicion >= 38:
                print("Gana Mike Tyson!")
                return c3.nombre
            if c4.posicion >= 38:
                print("Gana Estorbo!")
                return c4.nombre
            if c5.posicion >= 38:
                print("Gana Lentín!")
                return c5.nombre

        time.sleep(.2)
        os.system('cls')


saldo = 2000
print(" ██████╗ █████╗ ██████╗ ██████╗ ███████╗██████╗  █████╗     ██████╗ ███████╗     ██████╗ █████╗ ██████╗  █████╗ ██╗     ██╗      ██████╗ ███████╗",
            "\n██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗    ██╔══██╗██╔════╝    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██║     ██║     ██╔═══██╗██╔════╝",
            "\n██║     ███████║██████╔╝██████╔╝█████╗  ██████╔╝███████║    ██║  ██║█████╗      ██║     ███████║██████╔╝███████║██║     ██║     ██║   ██║███████╗",
            "\n██║     ██╔══██║██╔══██╗██╔══██╗██╔══╝  ██╔══██╗██╔══██║    ██║  ██║██╔══╝      ██║     ██╔══██║██╔══██╗██╔══██║██║     ██║     ██║   ██║╚════██║",
            "\n╚██████╗██║  ██║██║  ██║██║  ██║███████╗██║  ██║██║  ██║    ██████╔╝███████╗    ╚██████╗██║  ██║██████╔╝██║  ██║███████╗███████╗╚██████╔╝███████║",
            "\n ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚══════╝     ╚═════╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝"
        )
while saldo>0:
    print("Saldo:", saldo)
    seguir=input('Jugar? s/n: ')
    if seguir.lower()=='s':
        apuesta = int(input("Indique su apuesta: "))
        saldo -= apuesta
    else:
        break
    caballo = input("Indique el caballo al que apuesta: (Juan, Speedy, Mike Tyson, Estorbo, Lentín): ")
    ganador = jugar()

    c1.posicion = 0
    c2.posicion = 0
    c3.posicion = 0
    c4.posicion = 0
    c5.posicion = 0

    if caballo == ganador:
        saldo += apuesta*4.5
        print("ACERTASTE!!!!")
    else:
        print("PERDISTE :(")

if saldo<=0:
    print('Estas sin dinero :(')