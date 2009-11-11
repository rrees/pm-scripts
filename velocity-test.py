from velocity import calculate_weeks
def test_week_calcuation():
	assert 2 == calculate_weeks(points = 20, velocity = 5, team_capacity = 2 )