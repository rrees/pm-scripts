from datetime import date, timedelta, date
from velocity import calculate_weeks, end_date, velocity_calculator_maker, points_delivered_until, velocity_required_for
from project import Project
from projections import project_projections, date_projections


def format_date(date):
	return date.strftime("%d/%m/%Y")

yw_velocity = 5
model_velocity = 5
high_velocity = 10
low_velocity = 7

total_scope = 192
dev_complete = 64
remaining_scope = total_scope - dev_complete

		
	
project_details = Project()

project_details.total_scope = 192
project_details.dev_complete = 64
project_details.holiday_weeks = 0
project_details.yesterdays_weather = 5


project_projections(project_details)
date_projections(project_details)