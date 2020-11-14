# availability_check

Hello! This Programm kann help you to know, whether your Server is working. 
The Script will check your Server each 60 Secund to give you a 100% 
confidence, that you do not miss a crash.

To use this Script, you need:

1. Clone this Repository:
git clone https://github.com/Revtan18/availability_check

2. Install some python libs:
pip3 install twilio
pip3 install python-dotenv

3. Create a .env file (for example with nano editor - nano .env)

4. Copy this variables and write your data:
  TWILIO_ACCOUNT_SID = 
  TWILIO_AUTH_TOKEN = 
  URL = 
  SMS = 
  FROM_NUMBER = 
  MY_NUMBER = 
  
! URL - Server's name
! SMS - Your massage if the server do not work
! FROM_NUMBER - number, which will send you a massage
!MY_NUMBER - number, which will get a message

5. run availability.py



