import os
from twilio.rest import Client


class messageService:
    def __init__(self, account_sid, auth_token, phone_number, user_phone_number):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.phone_number = phone_number
        self.user_phone_number = user_phone_number
        self.client = Client(account_sid, auth_token)

    # Costs $0.0075
    def sendMealReminder(self, time: int):
        timeMap = {
            0: 'breakfast',
            1: 'lunch',
            2: 'dinner'
        }
        messageBody = f'Remember to eat {timeMap[time]}!'
        try:
            message = self.client.messages.create(
                body=messageBody,
                from_=self.phone_number,
                to=self.user_phone_number
            )
            print(f'Sent to {self.user_phone_number}: {messageBody}')
        except Exception as e:
            print('Error occured: ')
            print(e)
