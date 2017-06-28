import datetime
import sys
import os

# Basics Ed 2

from os import getcwd
where_am_I = getcwd()
print(where_am_I)

print(datetime.date.isoformat(datetime.date.today()))

import time
print(time.strftime("%H:%M"))
print(time.strftime("%A %p"))