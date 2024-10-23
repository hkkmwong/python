from datetime import datetime
from dateutil import relativedelta

# get two dates
d1 = input('First date (dd/mm/yyyy): ')
d2 = input('Second date (dd/mm/yyyy): ')

# convert string to date object
start_date = datetime.strptime(d1, "%d/%m/%Y")
end_date = datetime.strptime(d2, "%d/%m/%Y")

# Get the relativedelta between two dates
delta = relativedelta.relativedelta(end_date, start_date)
print('Years, Months, Days between two dates is')
print(delta.years, 'Years,', delta.months, 'months,', delta.days, 'days')
