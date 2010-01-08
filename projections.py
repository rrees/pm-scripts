from velocity import end_date, velocity_calculator_maker, points_delivered_until, velocity_required_for
from datetime import date

def format_date(date):
	return date.strftime("%d/%m/%Y")

def project_projections(project):

	velocity_calculator = velocity_calculator_maker(target_points = project.remaining_scope, capacity = 2)

	predictions = (("Yesterday's Weather", project.velocity.yesterday, velocity_calculator(velocity = project.velocity.yesterday)),
		('Model', project.velocity.model, velocity_calculator(velocity = project.velocity.model)),
		('Low', project.velocity.low, velocity_calculator(velocity = project.velocity.low)),
		('Target', project.velocity.high, velocity_calculator(velocity = project.velocity.high) ))
	
	for description, velocity, weeks in predictions:
		print "%s Velocity (%d), end date: %s" % (description, velocity, format_date(end_date(weeks)))

def date_projections(project):
	significant_dates = (('March', date(day = 1, month = 3, year = 2010)),)

	for label, finish in significant_dates:
		print "%s points for YWV %d" % (label, points_delivered_until(finish, velocity = project.velocity.yesterday, capacity = 2))

	target_dates = (('24th February', date(day = 24, month = 2, year = 2010)), ('24th March', date(day = 24, month = 3, year = 2010)))

	for label, target_date in target_dates:
		print "To meet a date of %s a velocity of %d is required" % (label, velocity_required_for(end_date = target_date, start_date = date.today(), target_points = project.remaining_scope, capacity = 2))
