import os
from dotenv import load_dotenv
from messageService import messageService
from clockService import clockService
from interfaceManager import interfaceManager

# Load environment variables
load_dotenv(os.path.join('./', '.env'))

# twilio account information
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
phone_number = os.getenv('TWILIO_PHONE_NUMBER')


def subscribeUser():
    """Subscribe a user to the messaging service"""
    # Get user information
    cli_interface = interfaceManager()
    answers = cli_interface.getUserInfo()
    user_phone_number = answers['phone_number']
    time_zone = answers['time_zone']
    # SMS messaging service
    message_service = messageService(
        account_sid, auth_token, phone_number, user_phone_number
    )
    # Periodic checking service
    clock_service = clockService(time_zone)
    clock_service.waitForMeal(
        # callback=message_service.sendMealReminder
        callback=lambda x: print(x)
    )


subscribeUser()
