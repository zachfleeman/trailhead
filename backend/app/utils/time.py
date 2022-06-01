import dateparser

def parse_human_readable_time(time_string):
    return dateparser.parse(time_string, settings={'RETURN_AS_TIMEZONE_AWARE': True})