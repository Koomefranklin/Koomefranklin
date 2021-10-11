# importing date and time to work with dates
from datetime import datetime
from dateutil.parser import parse #parse helps read strings as dates
b = input("Imput the time in mm/dd/yyyy formart")#getting user input dates
a = parse(b, datefirst) #turning the string to date fprmart
c = datetime.date(a)
d = c.strftime("%#d/%#m/%Y")
print(d)
