from datetime import date, timedelta, date
from velocity import calculate_weeks, end_date, velocity_calculator_maker, points_delivered_until, velocity_required_for, Velocity
from project import Project
from projections import project_projections, date_projections


yw_velocity = 5
model_velocity = 5
high_velocity = 10
low_velocity = 7

total_scope = 192
dev_complete = 64
remaining_scope = total_scope - dev_complete

velocity_model = Velocity(model_velocity = 5, low_velocity = 7, high_velocity = 10, yesterdays_velocity = 5)		
	
project_details = Project(velocity = velocity_model, total_scope = 192, dev_complete = 64)

project_details.holiday_weeks = 0


project_projections(project_details)
date_projections(project_details)