
from project import Project

def test_project_should_calculate_the_remaining_scope():
	project = Project(total_scope = 60, dev_complete = 23)
	assert project.remaining_scope == (60 - 23)

def test_project_should_have_yesterdays_weather():
	project = Project(yesterdays_weather = 33)
	assert project.yesterdays_weather == 33