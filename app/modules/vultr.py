import os
import requests
import tabulate
import app.main as main
from dotenv import load_dotenv

load_dotenv()

vultr_url = os.getenv('vultr_url')
vultr_token = os.getenv('vultr_token')

def get(vultr_url, endpoint, vultr_token):
    headers = {"Authorization": "Bearer " + vultr_token}
    if endpoint == 'account':
        r = requests.get(vultr_url + endpoint, headers=headers).json()
        account_data = r['account']
        return(account_data)
    elif endpoint == 'instances':
        r = requests.get(vultr_url + endpoint, headers=headers).json()
        instances_data = r['instances']
        return(instances_data)

def accounts():
    account_data = get(vultr_url, 'account', vultr_token)
    account_list = list(account_data.items())
    print("Account Details:")
    print(tabulate.tabulate(account_list, headers='firstrow', tablefmt='simple_grid', maxcolwidths=[None, 32]))

def instances():
    instances_data = get(vultr_url, 'instances', vultr_token)
    instances_list = list(instances_data[0].items())
    print("Instances:")
    print(tabulate.tabulate(instances_list, headers='firstrow', tablefmt='simple_grid', maxcolwidths=[None, 32]))

def menu():
    running = True
    while running == True:
        selection = int(input("What would you like to do ? \n 1. Get Vultr Account details \n 2. Get Vultr Instance details \n 0. Return to the main menu. \n \n"))
        if selection == 1:
            accounts()
        elif selection == 2:
            instances()
        elif selection == 0:
            running = False
    else:
        main.main_menu()