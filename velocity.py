from datetime import date, timedelta

class Velocity:
	def __init__(self, model_velocity):
		self.model = model_velocity

def calculate_weeks(points = 221 - 26, velocity = 5, team_capacity = 2):
	return points / (velocity * team_capacity)

def end_date(weeks, holiday_weeks = 2, start_date = date.today()):
	return start_date + timedelta(weeks = weeks + holiday_weeks)

def velocity_calculator_maker(target_points, capacity):
	return lambda total_points = target_points, velocity = 5, team_capacity = capacity: total_points / (velocity * team_capacity)
	
def points_delivered_until(date, start_date = date.today(), velocity = 5, holiday_weeks = 0, capacity = 2):
	def to_days(weeks):
		return weeks * 7

	return (((date - start_date).days - (to_days(holiday_weeks))) / 7) * (velocity * capacity)

def velocity_required_for(start_date, end_date, target_points, capacity = 1, holiday_weeks = 0):
	weeks =  weeks_between(start_date, end_date) - holiday_weeks
	velocity = (target_points / capacity) / weeks
	return velocity

def weeks_between(start_date, end_date):
	weeks = 0
	days_between = (end_date - start_date).days
	if(days_between%7 > 0): weeks = weeks + 1
	return  weeks + (days_between/ 7)
