import os
from dotenv import load_dotenv
from twilio.rest import Client
from messageService import messageService
from clockService import clockService

# Load environment variables
load_dotenv(os.path.join('./', '.env'))

# twilio account information
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
phone_number = os.getenv('TWILIO_PHONE_NUMBER')
user_phone_number = '+14085136711'


messageService = messageService(
    account_sid, auth_token, phone_number, user_phone_number
)
clockService = clockService(-8)
clockService.waitForMeal(
    callback=messageService.sendMealReminder
)
