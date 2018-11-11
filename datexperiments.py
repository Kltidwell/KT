#date experiments
import time
from datetime import date, datetime, timedelta

startDate = date(2016, 1, 1)
endDate = date(2017, 12, 31)

# span = (endDate - startDate)

# newDate = span/4 + startDate

# newEnd = (endDate-startDate)/2 + startDate

# newStart = startDate.replace(day = startDate.day + 1)


newStart = endDate + timedelta(days=1) 


# print('newStart')
print(newStart)
# print('newEnd')
# print(newEnd)