from velocity import velocity_calculator_maker, calculate_weeks, end_date, points_delivered_until
from datetime import date

eighteenth_november = date(day = 18, month = 11, year = 2009)
twenty_fifth_november = date(day = 25, month = 11, year = 2009)

def test_week_calcuation():
	assert 2 == calculate_weeks(points = 20, velocity = 5, team_capacity = 2 )

def test_end_date_calculation():
	an_end_date = end_date(start_date = eighteenth_november, weeks = 1, holiday_weeks = 0)
	assert 25 == an_end_date.day
	assert 11 == an_end_date.month
	assert 2009 == an_end_date.year
	
def test_velocity_calculator_maker():
	velocity_calculator = velocity_calculator_maker(target_points = 20, capacity = 2)
	
	assert calculate_weeks(points = 20, velocity = 5, team_capacity = 2) == velocity_calculator(velocity = 5)

def test_points_delivered_until():
	assert 20 == points_delivered_until(twenty_fifth_november, capacity = 2, velocity = 10, holiday_weeks = 0)