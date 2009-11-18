from datetime import date, timedelta, date
from velocity import calculate_weeks, end_date

def format_date(date):
	return date.strftime("%d/%m/%Y")

yw_velocity = 5
model_velocity = 5
high_velocity = 10
low_velocity = 7


print "Yesterday's Weather Velocity (%d), end date: %s" % (yw_velocity, format_date(end_date(calculate_weeks(velocity = yw_velocity))))

print "Model Velocity (%d), end date: %s" % (model_velocity,  format_date(end_date(calculate_weeks())))

print "Low Velocity (%d), end date: %s" % (low_velocity, format_date(end_date(calculate_weeks(velocity = low_velocity))))

print "Target Velocity (%d), end date: %s" % (high_velocity, format_date(end_date(calculate_weeks(velocity= high_velocity))))

def to_days(weeks):
	return weeks * 7

def points_delivered_until(date, velocity = 5, holiday_weeks = 2, capacity = 2):
	return (((date - date.today()).days - (to_days(holiday_weeks))) / 7) * (velocity * capacity)

print "March points for YWV %d" %(points_delivered_until(date(day = 1, month = 3, year = 2010), velocity = 3, capacity = 2))
