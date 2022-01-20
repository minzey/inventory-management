from datetime import datetime

import pytz
from django.utils import timezone


def convert_to_localtime_str(dt_datetime):
    """
    Returns the string equivalent of datetime object in django timezone. If datetime object has no timezone info,
    then it is assumed to be in UTC.
    :param dt_datetime: datetime object
    :return: string in localtime in the format mm/dd/YYYY HH:MM:SS
    """

    if dt_datetime.tzinfo == None:
        dt_datetime.replace(tzinfo=pytz.UTC)
    return datetime.strftime(timezone.localtime(dt_datetime), "%m/%d/%Y %H:%M:%S")