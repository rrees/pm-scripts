from velocity import calculate_weeks, end_date
from datetime import date

def test_week_calcuation():
	assert 2 == calculate_weeks(points = 20, velocity = 5, team_capacity = 2 )

def test_end_date_calculation():
	an_end_date = end_date(start_date = date(day = 18, month = 11, year = 2009), weeks = 1, holiday_weeks = 0)
	assert 25 == an_end_date.day