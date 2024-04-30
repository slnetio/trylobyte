import requests
def get(vultr_url, endpoint, vultr_token):
    headers = {"Authorization": "Bearer " + vultr_token}
    if endpoint == 'account':
        accounts = requests.get(vultr_url + endpoint, headers=headers).json()
        return(accounts)
    elif endpoint == 'instances':
        instances = requests.get(vultr_url + endpoint, headers=headers).json()
        return(instances)