import pytz


def timezones(request):
    """
    Context processor to make 'timezones' context available in all templates of the application.
    :param request:
    :return:
    """
    return {'timezones': pytz.common_timezones}