def ruleta():
    print(
    "   ███████████   █████  █████ █████       ██████████ ███████████   █████████   \n"
    "  ░░███░░░░░███ ░░███  ░░███ ░░███       ░░███░░░░░█░█░░░███░░░█  ███░░░░░███  \n"
    "   ░███    ░███  ░███   ░███  ░███        ░███  █ ░ ░   ░███  ░  ░███    ░███  \n"
    "   ░██████████   ░███   ░███  ░███        ░██████       ░███     ░███████████  \n"
    "   ░███░░░░░███  ░███   ░███  ░███        ░███░░█       ░███     ░███░░░░░███  \n"
    "   ░███    ░███  ░███   ░███  ░███      █ ░███ ░   █    ░███     ░███    ░███  \n"
    "   █████   █████ ░░████████   ███████████ ██████████    █████    █████   █████ \n"
    "   ░░░░░   ░░░░░   ░░░░░░░░   ░░░░░░░░░░░ ░░░░░░░░░░    ░░░░░    ░░░░░   ░░░░░ ")


from select import select
from socket import socket
import time
import random
from prettytable import PrettyTable
import os
from playsound import playsound
 
 
tiradas=0
lista_numeros=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,35,36]
numeros_verdes=[0]
numeros_rojos=[1,3,5,7,9,12,14,16,18,20,21,23,25,27,29,31,32,34,36]
numeros_negros=[2,4,6,8,10,11,13,15,17,19,22,24,26,28,30,33,35]

x=PrettyTable()

x.field_names =['\x1b[5;30;42m'+' 0 '+'\x1b[0m','\x1b[4;30;41m'+' 1 '+'\x1b[0m','\x1b[5;30;47m'+' 2 '+'\x1b[0m','\x1b[4;30;41m'+' 3 '+'\x1b[0m','\x1b[5;30;47m'+' 4 '+'\x1b[0m','\x1b[4;30;41m'+' 5 '+'\x1b[0m','\x1b[5;30;47m'+' 6 '+'\x1b[0m','\x1b[4;30;41m'+' 7 '+'\x1b[0m','\x1b[5;30;47m'+' 8 '+'\x1b[0m','\x1b[4;30;41m'+' 9 '+'\x1b[0m','\x1b[5;30;47m'+' 10 '+'\x1b[0m','\x1b[5;30;47m'+' 11 '+'\x1b[0m','\x1b[4;30;41m'+' 12 '+'\x1b[0m','\x1b[5;30;47m'+' 13 '+'\x1b[0m','\x1b[4;30;41m'+' 14 '+'\x1b[0m','\x1b[5;30;47m'+' 15 '+'\x1b[0m','\x1b[4;30;41m'+' 16 '+'\x1b[0m','\x1b[5;30;47m'+' 17 '+'\x1b[0m','\x1b[4;30;41m'+' 18 '+'\x1b[0m']

x.add_row(['\x1b[5;30;47m'+' 19 '+'\x1b[0m','\x1b[4;30;41m'+' 20 '+'\x1b[0m','\x1b[4;30;41m'+' 21 '+'\x1b[0m','\x1b[5;30;47m'+' 22 '+'\x1b[0m','\x1b[4;30;41m'+' 23 '+'\x1b[0m','\x1b[5;30;47m'+' 24 '+'\x1b[0m','\x1b[4;30;41m'+' 25 '+'\x1b[0m','\x1b[5;30;47m'+' 26 '+'\x1b[0m','\x1b[4;30;41m'+' 27 '+'\x1b[0m','\x1b[5;30;47m'+' 28 '+'\x1b[0m','\x1b[4;30;41m'+' 29 '+'\x1b[0m','\x1b[5;30;47m'+' 30 '+'\x1b[0m','\x1b[4;30;41m'+' 31 '+'\x1b[0m','\x1b[4;30;41m'+' 32 '+'\x1b[0m','\x1b[5;30;47m'+' 33 '+'\x1b[0m','\x1b[4;30;41m'+' 34 '+'\x1b[0m','\x1b[5;30;47m'+' 35 '+'\x1b[0m','\x1b[4;30;41m'+' 36 '+'\x1b[0m','\x1b[4;30;40m'+'   '+'\x1b[0m'])

def tabla():
    print(x)

def menu():
    print('''
        MENÚ:
        1. Apostar número
        2. Apostar negro
        3. Apostar rojo
        4. Apostar verde
        5. Apostar pares
        6. Apostar impares
        7. Dejar de apostar
    ''')

def limpiar():
    time.sleep(3)
    os.system('cls')
    
choice=None
ruleta()
tabla()
playsound('./sonidos/temazo_ini.wav')
limpiar()

def eleccion():
    global choice, bank
    ruleta()
    tabla()
    menu()
    print("Bank: ",bank)
    numeros=[1,2,3,4,5,6,7]
    valid=False
    while valid==False and bank>0:
        try:
            choice = int(input("Que desea hacer: "))
            valid=True
            if choice not in numeros:
                raise Exception
        except Exception:
            print('Opción no disponible en el menú')
            valid=False 
        except:
            print('Error! volver a intentar')
            valid=False
    if valid==True:
        return True

bank = 1000

def apostar():
    global bank, apuesta, choice
    elegir=eleccion()
    if elegir==True and choice<7 and bank>0:
        valid2=False
        while valid2==False:
            try:
                apuesta = int(input("Ingrese la cantidad que quiere apostar: "))
                if apuesta>bank and bank>0:
                    print('No tienes suficiente dinero para esa apuesta')
                else:
                    valid2=True
            except:
                print('Error! volver a intentar')
##numero_apostado = int(input("Ingrese el numero al que quiere apostar: "))

##FUNCIONES 
 
def apuesta_num():
    global bank
    numero_ganador = random.choice(lista_numeros)
    print(x)
    print ("El numero premiado es:",numero_ganador)
    tiradas + 1
    if numero_ganador == 0:
        print("El numero ganador es el 00 !!")
        if numero_apostado == 0:
            bank = bank + apuesta * 12
            playsound('./sonidos/bonk.wav')
            print("Bank: ",bank)
        elif numero_apostado != 0:
            bank = bank - apuesta
            print("Bank: ",bank)
            playsound('./sonidos/bank.wav')
        
    elif numero_apostado == numero_ganador:
        print("Tu numero ha salido premiado !")
        bank = bank + apuesta * 5
        print("Bank: ", bank)
        playsound('./sonidos/bonk.wav')
    else:
        bank = bank - apuesta
        print("Tu numero no ha salido premiado !")
        print("Bank: ", bank)
        playsound('./sonidos/bank.wav')
        
        
def apuesta_rojo():
    global bank
    numero_ganador = random.choice(lista_numeros)
    print(x)
    print ("El numero premiado es:",numero_ganador)
    tiradas + 1
    ##if numero_apostado in numeros_rojos:
    if numero_ganador in numeros_rojos:
        print("El color rojo ha salido premiado !")
        bank = bank + apuesta
        print("Bank: ",bank)
        playsound('./sonidos/bonk.wav')
    elif numero_ganador in numeros_negros:
        print("El color rojo no ha salido premiado...")
        bank = bank - apuesta
        print("Bank: ",bank)
        playsound('./sonidos/bank.wav')
    ##else:
        ##print("No se ha podido realizar la apuesta")
        
def apuesta_negro():
    global bank
    numero_ganador = random.choice(lista_numeros)
    print(x)
    print ("El numero premiado es:",numero_ganador)
    tiradas + 1
    ##if numero_apostado in numeros_negros:
    if numero_ganador in numeros_negros:
        print("El color negro ha salido premiado !")
        bank = bank + apuesta
        print("Bank: ",bank)
        playsound('./sonidos/bonk.wav')
    elif numero_ganador in numeros_rojos:
        print("El color negro no ha salido premiado...")
        bank = bank - apuesta
        print("Bank: ",bank)
        playsound('./sonidos/bank.wav')
    ##else:
        ##print("No se ha podido realizar la apuesta")
        
def apuesta_verde():
    global bank
    numero_ganador = random.choice(lista_numeros)
    print(x)
    print ("El numero premiado es:",numero_ganador)
    tiradas + 1
    if numero_ganador in numeros_verdes:
        print("El color verde ha salido premiado !!")
        bank = bank + apuesta * 12
        print("Bank: ",bank)
        playsound('./sonidos/bonk.wav')
    else:
        print("El color verde no ha salido premiado...")
        bank = bank - apuesta
        print("Bank: ",bank)
        playsound('./sonidos/bank.wav')
        
def apuesta_pares():
    global bank
    numero_ganador = random.choice(lista_numeros)
    print(x)
    print ("El numero premiado es:",numero_ganador)
    tiradas + 1
    if numero_ganador % 2 == 0:
        print("Los numeros pares han salido premiados !")
        bank = bank + apuesta * 3
        print("Bank: ",bank)
        playsound('./sonidos/bonk.wav')
    else:
        print("Los numeros pares no han salido premiados...")
        bank = bank - apuesta
        print("Bank: ",bank)
        playsound('./sonidos/bank.wav')
        
def apuesta_impares():
    global bank
    numero_ganador = random.choice(lista_numeros)
    print(x)
    print ("El numero premiado es:",numero_ganador)
    tiradas + 1
    if numero_ganador % 2 != 0:
        print("Los numeros impares han salido premiados !")
        bank = bank + apuesta * 3
        print("Bank: ",bank)
        playsound('./sonidos/bonk.wav')

    else:
        print("Los numeros impares no han salido premiados...")
        bank = bank - apuesta
        print("Bank: ",bank)
        playsound('./sonidos/bank.wav')
        
## EJECUCION PRINCIPAL
if bank>0:
    apostar()
else:
    print('Estas sin dinero!')

while bank>0:
    if choice == 1:
        valid=False
        while valid==False:
            try:
                numero_apostado = int(input("Ingrese el numero al que quiere apostar: "))
                valid=True 
                if numero_apostado not in lista_numeros:
                    raise Exception
            except Exception:
                print('Este número no está en la lista')
                valid=False
            except:
                print('Error! volver a intentar')
                valid=False
        apuesta_num()
        limpiar()
        apostar()

    elif choice == 2:
        apuesta_negro()
        limpiar()
        apostar()

    elif choice == 3:
        apuesta_rojo()
        limpiar()
        apostar()

    elif choice == 4:
        apuesta_verde()
        limpiar()
        apostar()

    elif choice == 5:
        ##numero_apostado = int(input("Ingrese el numero al que quiere apostar: "))
        apuesta_pares()
        limpiar()
        apostar()

    elif choice == 6:
        ##numero_apostado = int(input("Ingrese el numero al que quiere apostar: "))
        apuesta_impares()
        limpiar()
        apostar()
    
    elif choice ==7:
        print('EXIT')
        limpiar()
        break
        
    if bank <= 0:
        print("Se te acabó el dinero :(")
        playsound('./sonidos/bank.wav')
        limpiar()
        break