# -*- coding: utf-8 -*-

"""
Filename: __init__.py
Date: 2020-07-07 11:12:38
Title: idate
"""

from copy import deepcopy

from collections import namedtuple
from datetime import datetime
from datetime import timedelta

import tzlocal
import pytz


class IDates:
    def __init__(self, timestamp=None, date=None, datetime=None, fmt="%Y-%m-%d %H:%M:%S"):
        self.init(timestamp, date, datetime, fmt)

    def init(self, timestamp=None, date=None, d=None, fmt="%Y-%m-%d %H:%M:%S"):
        if all(v is None for v in (timestamp, date, d)):
            self.date = datetime.now()
        elif timestamp is not None:
            self.init_from_timestamp(timestamp)
        elif date is not None:
            self.init_from_string(date, fmt)
        elif d is not None and isinstance(d, datetime):
            self.date = deepcopy(d)
        else:
            raise Exception("Please give me @timestamp or @date")

    @property
    def _local_tz(self):
        return tzlocal.get_localzone()

    @property
    def _utc(self):
        return pytz.timezone("UTC")

    @property
    def _etc_utc(self):
        return pytz.timezone("ETC/UTC")

    @property
    def _shanghai(self):
        return pytz.timezone("Asia/Shanghai")

    def init_from_timestamp(self, timestamp):
        self.date = datetime.fromtimestamp(timestamp)

    def init_from_string(self, date, fmt):
        self.date = datetime.strptime(date, fmt)

    def to_timestamp(self):
        """ datetime转成时间戳
        """
        return self.date.timestamp()

    def to_string(self, fmt="%Y-%m-%d %H:%M:%S"):
        """ datetime转成字符串
        """
        return self.date.strftime(fmt)

    def to_tz_string(self, tz, fmt="%Y-%m-%d %H:%M:%S"):
        """ 把self.date转成tz指定的时区
        """
        if isinstance(tz, str):
            tz = pytz.timezone(tz)
        return self.date.astimezone(tz).strftime(fmt)

    def days_jump(self, n):
        """ 如果n大于0,则返回n天后
        如果n小于0则返回n天前
        """
        delta = timedelta(n)
        return self.date + delta
