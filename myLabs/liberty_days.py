from datetime import datetime, date, timedelta


now = datetime.now()
start_date = datetime(2016, 9, 19)

date_calc = now - start_date

print(f'Total days at Liberty: {date_calc.days}')
years = int(date_calc.days / 365)
print(f'Total years at Liberty: {years}')