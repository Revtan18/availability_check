import requests, os, time, logging
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
URL = os.getenv('URL')
FROM_NUMBER = os.getenv('FROM_NUMBER')
MY_NUMBER = os.getenv('MY_NUMBER')
SMS = os.getenv('SMS')

def sms():
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body= SMS,  
        from_= FROM_NUMBER,  
        to= MY_NUMBER,  
        ) 
    return message.sid    

response = requests.get(URL)
URL_check = response.ok

while URL_check == True:
    logging.info('Checking server')
    time.sleep(60)
else:
    logging.error('МЫ ВСЁ УРОНИЛИ!!!11')
    sms()


