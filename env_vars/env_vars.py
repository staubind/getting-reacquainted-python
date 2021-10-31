# use python-dotenv
# allows the app to import vars in .env (from twilio - env variables python)
from dotenv import load_dotenv
import os
print(load_dotenv)
print(os.getcwd()+'/.env')
load_dotenv(os.getcwd()+'/.env')

print(os.environ.get('MY_KEY'))