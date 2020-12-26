from datetime import datetime, timedelta
import time
from threading import Timer


class clockService:
    # Timezone in the format of +/- UTC time
    # For example, pacific time is -8
    def __init__(self, timezoneOffset):
        self.timezoneOffset = timezoneOffset
        self.times = self.generateTimes()

    def generateTimes(self):
        # UTC Breakfast, lunch, dinner
        return [
            [7, 0, 0],
            [11, 0, 0],
            [17, 0, 0]
        ]

    def sleep(self, day=None, hour=None, minute=None, second=None):
        t1 = datetime.utcnow() + timedelta(hours=self.timezoneOffset)
        t2 = (t1 + timedelta(hours=self.timezoneOffset)).replace(
            day=day if day != None else t1.day,
            hour=hour if hour != None else t1.hour,
            minute=minute if minute != None else t1.minute,
            second=second if second != None else t1.second
        )
        delta_t = t2 - t1
        if delta_t.total_seconds() < 0:
            return -1
        time.sleep(delta_t.total_seconds())
        return 0

    def waitForMeal(self, callback):
        # Loop for automated texting
        # Setting this at 10 days for now
        for i in range(10):
            # Daily notifications
            for i, e in enumerate(self.times):
                if (self.sleep(hour=e[0], minute=e[1], second=e[2]) == -1):
                    continue
                callback(i)

            # Reset timer at end of day
            nextDay = datetime.utcnow() + timedelta(hours=self.timezoneOffset)
            self.sleep(
                day=nextDay.day + 1,
                hour=0,
                minute=0,
                second=0
            )
            print(f'Starting new day: {nextDay}')