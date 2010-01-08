
from project import Project
from velocity import Velocity

velocity_model = Velocity(model_velocity = 5)

def test_project_should_calculate_the_remaining_scope():
	project = Project(velocity = velocity_model, total_scope = 60, dev_complete = 23)
	assert project.remaining_scope == (60 - 23)

def test_project_should_have_yesterdays_weather():
	project = Project(velocity = velocity_model, yesterdays_weather = 33)
	assert project.yesterdays_weather == 33
	
def test_project_should_have_velocity_details():
	project = Project(velocity = velocity_model)
	assert project.velocity.model == 5
	
	