from datetime import datetime
now = datetime.now()
now.year
now.month
now.day
now.hour
now.minute
now.second

print '%4d/%2d/%2d %2d:%2d:%2d' % (now.year, now.month, now.day, now.hour, now.minute, now.second)
