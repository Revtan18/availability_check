import requests, os, time, logging
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
URL = os.getenv('URL')
TWILIO_NUMBER = os.getenv('TWILIO_NUMBER')
MY_NUMBER = os.getenv('MY_NUMBER')

def sms():
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body='Server is down. The End of the World',  
        from_= TWILIO_NUMBER,  
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


