#!/usr/bin/env python

import time

from datetime import datetime, timedelta

start_time = datetime.utcnow() + timedelta(seconds=10)
while datetime.utcnow() < start_time:
    print('Echo:', datetime.utcnow())
    time.sleep(.1)
