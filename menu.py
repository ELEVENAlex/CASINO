##menu to wapo
from subprocess import run
import sys
from playsound import playsound
import os

##modulos

def visual_casino():
    print('''                                                                                                
                                                                           d8b                   
                                                                           Y8P                   
                                                                                                
                                                 .d8888b  8888b.  .d8888b  888 88888b.   .d88b.  
                                                d88P"        "88b 88K      888 888 "88b d88""88b 
                                                888      .d888888 "Y8888b. 888 888  888 888  888 
                                                Y88b.    888  888      X88 888 888  888 Y88..88P 
                                                 "Y8888P "Y888888  88888P' 888 888  888  "Y88P"  
                                                    
    ''')

def visual_juegos():
    print('''
                                                    \x1b[1;37;40m+---------------------------------+\x1b[0m
                                                    \x1b[1;37;40m|\x1b[0m   \x1b[1;31;40m 1. TRAGAPERRAS              \x1b[0m \x1b[1;37;40m|\x1b[0m 
                                                    \x1b[1;37;40m|\x1b[0m   \x1b[1;34;40m 2. BLACKJACK                \x1b[0m \x1b[1;37;40m|\x1b[0m
                                                    \x1b[1;37;40m|\x1b[0m   \x1b[1;36;40m 3. CARRERA DE CABALLOS      \x1b[0m \x1b[1;37;40m|\x1b[0m
                                                    \x1b[1;37;40m|\x1b[0m   \x1b[1;33;40m 4. RULETA                   \x1b[0m \x1b[1;37;40m|\x1b[0m
                                                    \x1b[1;37;40m|\x1b[0m   \x1b[1;35;40m 5. BINGO                    \x1b[0m \x1b[1;37;40m|\x1b[0m
                                                    \x1b[1;37;40m+---------------------------------+\x1b[0m
                                                            
        ''')

def start():
    print(''' 
                                                               _                 _   
                                                         ___ _| |_ _____  ____ _| |_ 
                                                        /___|_   _|____ |/ ___|_   _)
                                                        |___ | | |_/ ___ | |     | |_ 
                                                        (___/   \__)_____|_|      \__)
                              
    ''')
    playsound('./sonidos/start_sound.wav')
def opciones():
    pregunta=input('''
                                                        Escoger juego
                                                        --> ''').lower()
    if pregunta=='1' or pregunta=='tragaperras':
        os.system('cls')
        start()
        import slots
    if pregunta=='2' or pregunta=='blackjack':
        os.system('cls')
        start()
        run([sys.executable,'BLACKJACK.py'])
    if pregunta=='3' or pregunta=='carrera de caballos':
        os.system('cls')
        start()
        import carr_caballos
    if pregunta=='4' or pregunta=='ruleta':
        os.system('cls')
        start()
        import ruleta2
    if pregunta=='5' or pregunta=='bingo':
        os.system('cls')
        start()
        run([sys.executable,'BingoProyecto.py'])
    else:
        return False

def menu():
    visual_casino()
    #sonido inicio
    playsound('./sonidos/temazo_ini.wav')
    #para en 5s
    visual_juegos()
    #sonido juegos
    playsound('./sonidos/start_sound.wav')
    menu_pregunta=False
    while menu_pregunta==False:
        os.system('cls')
        visual_casino()
        visual_juegos()
        menu_pregunta=opciones()
        os.system('cls')

menu()


