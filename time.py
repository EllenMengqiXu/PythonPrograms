#!/usr/bin/env python
# coding:utf8


import time
# local time will print out the timestamp of the current time. #timestamp
localtime = time.time()
print (localtime)

import datetime
# It will print out the date format of current time. #human friendly

lt=datetime.datetime.fromtimestamp(localtime).strftime('%Y-%m-%d %H:%M:%S')
print(lt)
