from datetime import date, timedelta, date
from velocity import calculate_weeks, end_date, velocity_calculator_maker

def format_date(date):
	return date.strftime("%d/%m/%Y")

yw_velocity = 5
model_velocity = 5
high_velocity = 10
low_velocity = 7

total_scope = 221
dev_complete = 26

velocity_calculator = velocity_calculator_maker(target_points = total_scope - dev_complete, capacity = 2)

predictions = (("Yesterday's Weather", yw_velocity, velocity_calculator(velocity = yw_velocity)),
	('Model', model_velocity, velocity_calculator(velocity = model_velocity)),
	('Low', low_velocity, velocity_calculator(velocity = low_velocity)),
	('Target', high_velocity, velocity_calculator(velocity = high_velocity) ))
	
for description, velocity, weeks in predictions:
	print "%s Velocity (%d), end date: %s" % (description, velocity, format_date(end_date(weeks)))

def to_days(weeks):
	return weeks * 7

def points_delivered_until(date, velocity = 5, holiday_weeks = 2, capacity = 2):
	return (((date - date.today()).days - (to_days(holiday_weeks))) / 7) * (velocity * capacity)

significant_dates = ( ('New Year', date(day= 4, month = 1, year = 2010)), ('March', date(day = 1, month = 3, year = 2010)))

for label, finish in significant_dates:
	print "%s points for YWV %d" % (label, points_delivered_until(finish, velocity = yw_velocity, capacity = 2))

