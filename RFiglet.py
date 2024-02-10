import pyfiglet
import random
from colorama import Fore, Style
import time

def init_colorama():
    try:
        from colorama import init
        init()
    except ImportError:
        print("Assicurati di aver installato la libreria 'colorama' con 'pip install colorama'.")

def type_effect_cyan(message):
    for char in message:
        print(Fore.CYAN + char, end='', flush=True)
        time.sleep(0.05)  # Puoi regolare la velocità dell'effetto modificando il valore qui

    print(Style.RESET_ALL)

def crea_testo_figlet():
    init_colorama()

    type_effect_cyan("Benvenuto nel convertitore di testo in stile figlet!")

    while True:
        colore_iniziale = random.choice([Fore.GREEN, Fore.CYAN, Fore.MAGENTA, Fore.YELLOW, Fore.BLUE])
        print(colore_iniziale, end='')

        testo_input = input("Inserisci il testo che vuoi convertire in stile figlet (scrivi 'exit' per uscire): ")

        if testo_input.lower() == 'exit':
            type_effect_cyan("Grazie per aver provato questo tool. Guarda altri script su t.me/VikingTerminal.")
            break

        stili_figlet = ["slant", "block", "isometric1", "isometric2", "caligraphy", "big", "small", "smslant", "chunky", "digital", "rectangles"]
        stile_casuale = random.choice(stili_figlet)
        ascii_art = pyfiglet.figlet_format(testo_input, font=stile_casuale)
        colore_casuale = random.choice([Fore.GREEN, Fore.CYAN, Fore.MAGENTA, Fore.YELLOW, Fore.BLUE])

        print(colore_casuale + ascii_art + Style.RESET_ALL, end='')

# Chiama la funzione per creare il testo come figlet con uno stile casuale
crea_testo_figlet()
