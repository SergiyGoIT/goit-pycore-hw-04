import sys
import os
from colorama import init, Fore

init(autoreset=True)

def list_directory(path, indent=""):
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):  # Якщо це директорія
            print(Fore.BLUE + indent + "📂 " + item)
            list_directory(full_path, indent + "  ")  # Рекурсія для вкладених папок
        else:  # Якщо це файл
            print(Fore.GREEN + indent + "📜 " + item)

if len(sys.argv) > 1:
    list_directory(sys.argv[1])
else:
    print("⚠ Використання: python task3.py <шлях до директорії>")

# cd D:\Git_GoIT\goit-pycore-hw-04
# python task3.py "D://Git_GoIT//goit-pycore-hw-04//"