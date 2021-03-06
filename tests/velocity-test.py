from velocity import velocity_calculator_maker, calculate_weeks, end_date, points_delivered_until, velocity_required_for, weeks_between
from datetime import date

eighteenth_november = date(day = 18, month = 11, year = 2009)
twenty_fifth_november = date(day = 25, month = 11, year = 2009)

def test_week_calcuation():
	assert 2 == calculate_weeks(points = 20, velocity = 5, team_capacity = 2 )

def test_end_date_calculation():
	an_end_date = end_date(start_date = eighteenth_november, weeks = 1, holiday_weeks = 0)
	assert twenty_fifth_november == an_end_date
	
def test_velocity_calculator_maker():
	velocity_calculator = velocity_calculator_maker(target_points = 20, capacity = 2)
	
	assert calculate_weeks(points = 20, velocity = 5, team_capacity = 2) == velocity_calculator(velocity = 5)

def test_points_delivered_until():
	assert 20 == points_delivered_until(twenty_fifth_november, start_date = eighteenth_november, capacity = 2, velocity = 10, holiday_weeks = 0)

fourth_january	= date(day = 4, month = 1, year = 2010)
eighteenth_january = date( day = 18, month = 1, year = 2010)

def test_velocity_required_to_deliver():
	velocity = velocity_required_for(start_date = fourth_january, end_date = eighteenth_january, capacity = 1, target_points = 20, holiday_weeks = 0)
	assert velocity == 10, "Expected 10, got %d" % (velocity, )

def test_weeks_calculator():
	weeks = weeks_between(start_date = date(day = 11, month = 1, year = 2010), end_date = date(day = 29, month = 1, year = 2010))
	assert weeks == 3, "Expected 3 weeks but got %d" % (weeks, )

