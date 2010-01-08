class Project:
	def __init__(self, velocity, total_scope = 0, dev_complete = 0, yesterdays_weather = 0):
		self.total_scope = total_scope
		self.dev_complete = dev_complete
		
		self.yesterdays_weather = yesterdays_weather
		self.velocity = velocity
		
		self.remaining_scope = self.total_scope - self.dev_complete
