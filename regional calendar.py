from datetime import datetime
from dateutil.parser import parse
b = input()
a = parse(b, datefirst)
c = datetime.date(a)
d = c.strftime("%#d/%#m/%Y")
print(d)
