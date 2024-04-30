import os
import json
import tabulate
from integrations import vultr

selection = int
def main_menu():
    print("1. Get information from Vultr")
    print("2. Quit")
    selection = int(input("What would you like to do? "))
    if selection == 1:
        vultr.menu()
    elif selection == 2:
        exit()

main_menu()