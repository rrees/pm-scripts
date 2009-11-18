from datetime import date, timedelta

def calculate_weeks(points = 221 - 26, velocity = 5, team_capacity = 2):
	return points / (velocity * team_capacity)

def end_date(weeks, holiday_weeks = 2, start_date = date.today()):
	return start_date + timedelta(weeks = weeks + holiday_weeks)

def velocity_calculator_maker(target_points, capacity):
	return lambda total_points = target_points, velocity = 5, team_capacity = capacity: total_points / (velocity * team_capacity)