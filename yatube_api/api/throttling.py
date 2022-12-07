import datetime

from rest_framework.throttling import BaseThrottle


class WorkingHoursRateThrottle(BaseThrottle):

    def allow_request(self, request, view):
        """С 3 до 5 часов ночи, запрещены запросы."""
        now = datetime.datetime.now().hour
        if now >= 3 and now <= 5:
            return False
        return True