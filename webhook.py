# Coded by 7b3087

import os 
import time 
import colorama 
from colorama import Fore
from dhooks import Webhook 
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("Webhook-spam <3")
colorama.init(autoreset=True)

def cls():
    os.system('cls')

rouge = Fore.RED
bleu = Fore.BLUE
vert = Fore.GREEN
blanc = Fore.WHITE

banner = """ 

 █     █░▓█████  ▄▄▄▄    ██░ ██  ▒█████   ▒█████   ██ ▄█▀
▓█░ █ ░█░▓█   ▀ ▓█████▄ ▓██░ ██▒▒██▒  ██▒▒██▒  ██▒ ██▄█▒ 
▒█░ █ ░█ ▒███   ▒██▒ ▄██▒██▀▀██░▒██░  ██▒▒██░  ██▒▓███▄░ 
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀  ░▓█ ░██ ▒██   ██░▒██   ██░▓██ █▄ 
░░██▒██▓ ░▒████▒░▓█  ▀█▓░▓█▒░██▓░ ████▓▒░░ ████▓▒░▒██▒ █▄
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒
  ▒ ░ ░   ░ ░  ░▒░▒   ░  ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░
  ░   ░     ░    ░    ░  ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░ 
    ░       ░  ░ ░       ░  ░  ░    ░ ░      ░ ░  ░  ░  
"""

print(bleu + banner)

def send_messages(webhook_url, num_messages, message, webhook_name=None, delay=0):
    hook = Webhook(webhook_url)

    message_counter = 0

    if webhook_name:
        hook.username = webhook_name 

        for _ in range(num_messages):
            try:
                hook.send(message)
                message_counter += 1
                cls()
                print(bleu + banner)
                print(f"{vert}[+] Les messages sont en cours d'envoi ! Nombre total de messages envoyés: {message_counter}")
                time.sleep(delay)

            except Exception as e:
                print(f"{rouge}[-] L'envoi des messages a échoué. ")
            
        print(f"{vert}[+] Tous les messages ont bien été envoyés !")
        time.sleep(3)
        cls()
        print(bleu + banner)

while True:
    webhook_url = input(f"{blanc}[+] Intégrez votre webhook: ")
    number = int(input(f"{blanc}[+] Quel est le nombre de messages: "))
    message = input(f"{blanc}[+] Quel message voulez-vous envoyer: ")   
    delay = input(f"{blanc}[+] Veuillez entre un delay entre chaque message: ")

    if delay:
        delay = float(delay)
    else:
        delay = 0

    webhook_name = input(f"{blanc}[+] Veuillez indiquer le nom de votre webhook (enter = skip): ")

    if webhook_name:
        send_messages(webhook_url, number, message, webhook_name, delay)
    else:
        send_messages(webhook_url, number, message, delay)
        input("7b3087 <3")


