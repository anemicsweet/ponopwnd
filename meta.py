#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# file for functions to get date/time sunrise/sunset/exact hours
# file to functions to determine current season
import suntime
from suntime import Sun
from datetime import date

today = date.today()
year = int(today.strftime("%Y"))
month = int(today.strftime("%m"))
day = int(today.strftime("%d"))


def get_sunset(year, month, day, lat, long):
    location = Sun(lat, long)
    ss = location.get_sunrise_time(year, month, day)
    return ss


def get_sunrise(year, month, day, lat, long):
    location = Sun(lat, long)
    sr = location.get_sunrise_time(year, month, day)
    return sr


print(get_sunrise(year, month, day, 50, 10))
