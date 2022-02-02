# line breake
from datetime import datetime

st01 = "i can \ndo it"
print(st01)

# to erase last letter

st02 = "flowers\b"
print(st02)

# add two lines

st03 = "i can"
st04 = "do"

print(st03, end=' ')
print(st04)

# formatting
st05 = "today is {0} , month is {1} , year is {2} and time is {3}"

print(st05.format("sunday", "july", "2021", "6.15"))
print(st05.format("monday", "may", "2021", "7.30"))

# format date and time

date_string = datetime(year=2021, month=8, day=22)
print(f"It is {date_string: %d, %b, %y} today")