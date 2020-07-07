# -*- coding: utf-8 -*-

"""
Filename: __init__.py
Date: 2020-07-07 11:12:38
Title: idate
"""

from collections import namedtuple
from datetime import datetime
from datetime import timedelta

import tzlocal
import pytz


class IDates:
    def __init__(self, timestamp=None, date=None, fmt="%Y-%m-%d %H:%M:%S"):
        self._local_tz = tzlocal.get_localzone()
        if timestamp is None and date is None:
            self.date = datetime.now(self._local_tz)
        elif timestamp is not None:
            self.init_from_timestamp(timestamp)
        elif date is not None:
            self.init_from_string(date, fmt)
        else:
            raise Exception("Please give me @timestamp or @date")

    def init_from_timestamp(self, timestamp):
        self.date = datetime.fromtimestamp(timestamp)

    def init_from_string(self, date, fmt):
        self.date = datetime.strptime(date, fmt)

    def timestamp(self):
        return self.date.timestamp()

    def string(self, fmt="%Y-%m-%d %H:%M:%S"):
        return self.date.strftime(fmt)

    def timestamp_to_tz(self, to_tz):
        to_tz = pytz.timezone(to_tz)
        return to_tz.localize(self.date).timestamp()

    def string_to_tz(self, to_tz, fmt="%Y-%m-%d %H:%M:%S"):
        to_tz = pytz.timezone(to_tz)
        date = to_tz.localize(self.date)
        return date.strftime(fmt)

if __name__ == '__main__':
    import time
    obj = IDates(date="2020-09-01", fmt="%Y-%m-%d")
    print(obj.timestamp())
    print(obj.timestamp_to_tz("UTC"))
    print(obj.string())
    print(obj.string_to_tz("UTC"))

    obj = IDates(timestamp=1598889600)
    print(obj.timestamp())
    print(obj.timestamp_to_tz("UTC"))
    print(obj.string())
    print(obj.string_to_tz("UTC"))
