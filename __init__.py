# -*- coding: utf-8 -*-

"""
Filename: __init__.py
Date: 2020-07-07 11:12:38
Title: idate
"""

from collections import namedtuple
from datetime import datetime
from datetime import timedelta

import pytz


class IDates:
    def __init__(self, timezone="UTC"):
        self.timezone = pytz.timezone(timezone)

    def timestamp_to_string(self, timestamp, fmt="%Y-%m-%d %H:%M:%S"):
        """
        1. timestamp: 时间戳
        2. fmt: 转换后字符串的格式
        """
        date = datetime.fromtimestamp(timestamp)
        date = date.astimezone(self.timezone)
        return date.strftime(fmt)

    def string_to_timestamp(self, date, fmt="%Y-%m-%d %H:%M:%S"):
        """
        1. date: 字符串格式
        2. fmt: date必须符合fmt
        """
        date = datetime.strptime(date, fmt)
        date = date.astimezone(self.timezone)
        return date.timestamp()

    def timestamp_to_datetime(self, timestamp):
        date = datetime.fromtimestamp(timestamp)
        date = date.astimezone(self.timezone)
        return date

    def string_to_datetime(self, date, fmt="%Y-%m-%d %H:%M:%S"):
        date = datetime.strptime(date, fmt)
        date = date.astimezone(self.timezone)
        return date

    def datetime_to_string(self, date, fmt="%Y-%m-%d %H:%M:%S"):
        date = date.astimezone(self.timezone)
        return date.strftime(fmt)

    def get_timestamp_range(self, start_timestamp, delta, is_zero=True):
        TimeRange = namedtuple("TimeRange", ["start", "end"])
        delta = timedelta(delta)
        date = self.timestamp_to_datetime(start_timestamp)
        date2 = date + delta
        if is_zero:
            date = date.replace(hour=0, minute=0, second=0)
            date2 = date2.replace(hour=0, minute=0, second=0)
        if delta.days >= 0:
            return TimeRange(start=date.timestamp(), end=date2.timestamp())
        else:
            return TimeRange(start=date2.timerange(), end=date.timestamp())

    def get_date_range(self, start_timestamp, end_timestamp, fmt="%Y-%m-%d %H:%M:%S"):
        return self.get_date_range_steps(start_timestamp, end_timestamp, fmt, 1)

    def get_date_range_steps(self, start_timestamp, end_timestamp, fmt="%Y-%m-%d %H:%M:%S", steps=1):
        DateRange = namedtuple("DateRange", ["start", "end"])
        start_date = self.timestamp_to_datetime(start_timestamp)
        end_date = self.timestamp_to_datetime(end_timestamp)
        days = (end_date - start_date).days
        while days - steps > 0:
            next_date = start_date + timedelta(steps)
            start_date_str = self.datetime_to_string(start_date, fmt=fmt)
            next_date_str = self.datetime_to_string(next_date, fmt=fmt)
            yield DateRange(start=start_date_str, end=next_date_str)
            start_date += timedelta(steps)
            days -= steps

        if days > 0:
            next_date = start_date + timedelta(abs(days))
            start_date_str = self.datetime_to_string(start_date, fmt=fmt)
            next_date_str = self.datetime_to_string(next_date, fmt=fmt)
            yield DateRange(start=start_date_str, end=next_date_str)
