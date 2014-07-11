#!/bin/env python

from datetime import datetime
now = datetime.now()

date = "%s/%s/%s" % (now.month, now.day, now.year)
time = "%s:%s:%s" % (now.hour, now.minute, now.second)

print "Current Date/Time: %s %s" % (date, time)
