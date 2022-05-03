### SAMPLE PRACTICE CODE for working and dealing with TIME and DATES ###

import datetime as dt
from datetime import datetime, deltatime, timezone
import tz

dt.tz_localize('America/Houston')
dt.tz_convert('America/Houston')
