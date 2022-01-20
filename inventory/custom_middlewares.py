import pytz

from django.utils import timezone

class TimezoneMiddleware:
    """
    Middleware to change the current timezone context of the application to the timezone set by the user.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tzname = request.session.get('django_timezone')
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()
        return self.get_response(request)