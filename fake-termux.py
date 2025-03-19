from colorama import Fore, Back, Style, init

import os

def clear_screen():
    # Для Linux/Android (Termux)
    os.system('clear')
    # Для Windows
    # os.system('cls')

# Очищаем экран при запуске программы
clear_screen()

init()

RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
RESET = '\033[0m'

print('''Welcome to Termux

Docs:       https://doc.termux.com
Community:  https://community.termux.com

Working with packages:
 - Search:  pkg search <query>
 - Install: pkg install <package>
 - Upgrade: pkg upgrade

Report issues at https://bugs.termux.com''')

while True:
    text = input(GREEN + '~ ' + RESET + '$ ')
    print('No command', text, 'found')