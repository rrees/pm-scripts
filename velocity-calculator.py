from datetime import date, timedelta, date

def calculate_weeks(points = 232, velocity = 5, team_capacity = 2):
	return points / (velocity * team_capacity)

def end_date(weeks, holiday_weeks = 2):
	return date.today() + timedelta(weeks = weeks + holiday_weeks)

def format_date(date):
	return date.strftime("%d/%m/%Y")

instinct_velocity = 3
model_velocity = 5
high_velocity = 10
low_velocity = 7


print "Yesterday's Weather Velocity (%d), end date: %s" % (instinct_velocity, format_date(end_date(calculate_weeks(velocity = instinct_velocity))))

print "Model Velocity (%d), end date: %s" % (model_velocity,  format_date(end_date(calculate_weeks())))

print "Low Velocity (%d), end date: %s" % (low_velocity, format_date(end_date(calculate_weeks(velocity = low_velocity))))

print "Target Velocity (%d), end date: %s" % (high_velocity, format_date(end_date(calculate_weeks(velocity= high_velocity))))

def to_days(weeks):
	return weeks * 7

def points_delivered_until(date, velocity = 5, holiday_weeks = 2):
	return (((date - date.today()).days - (to_days(holiday_weeks))) / 7) * velocity

print "March points for YWV %d" %(points_delivered_until(date(day = 1, month = 3, year = 2010), velocity = 3))