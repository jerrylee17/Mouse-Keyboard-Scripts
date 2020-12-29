import re
from PyInquirer import prompt
from prompt_toolkit.validation import Validator, ValidationError


class PhoneNumberValidator(Validator):
    def validate(self, document):
        ok = re.match(
            '^(\+?1[-]?)?\(?(\d{3})\)?[-]?(\d{3})[-]?(\d{4})$', document.text)
        if not ok:
            raise ValidationError(
                message='Please enter a valid phone number',
                cursor_position=len(document.text)
            )


class interfaceManager:
    # Get number and time zone
    def __init__(self):
        self.number = None
        self.timeZone = None

    def getUserInfo(self):
        questions = [
            {
                'type': 'input',
                'name': 'phone_number',
                'message': 'What is your phone number (xxx)xxx-xxxx? ',
                'validate': PhoneNumberValidator
            },
            {
                'type': 'list',
                'name': 'time_zone',
                'message': 'Choose your time zone',
                'choices': [
                    'UTC-08:00 (PT)',
                    'UTC-07:00 (MT)',
                    'UTC-06:00 (CT)',
                    'UTC-05:00 (ET)',
                ]
            }
        ]
        answers = prompt(questions)
        answers['time_zone'] = self.processTimeZone(answers['time_zone'])
        answers['phone_number'] = self.processPhoneNumber(
            answers['phone_number'])
        return answers

    def processTimeZone(self, time_zone_choice):
        convert_map = {
            'UTC-08:00 (PT)': -8,
            'UTC-07:00 (MT)': -7,
            'UTC-06:00 (CT)': -6,
            'UTC-05:00 (ET)': -5,
        }
        return convert_map[time_zone_choice]

    def processPhoneNumber(self, phone_number):
        entered_number = re.match(
            '^\+?(1)?[-]?\(?(\d{3})\)?[-]?(\d{3})[-]?(\d{4})$', phone_number)
        groups = entered_number.groups()
        ext = groups[0] or '1'
        number = '+' + ext + ''.join(groups[1:])
        return number


interface = interfaceManager()
answers = interface.getUserInfo()
print(answers)
