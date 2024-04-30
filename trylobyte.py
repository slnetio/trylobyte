import os
import vultr_api
from dotenv import load_dotenv

load_dotenv()

vultr_url = os.getenv('vultr_url')
vultr_key = os.getenv('vultr_key')

account_data = vultr_api.get(vultr_url, 'account', vultr_key)
instance_data = vultr_api.get(vultr_url, 'instances', vultr_key)

print(account_data['account']['name'])
print(instance_data['instances'][0]['id'])
print(instance_data['instances'][0]['label'])