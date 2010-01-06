class Project:
	def __init__(self, total_scope = 0, dev_complete = 0):
		self.total_scope = total_scope
		self.dev_complete = dev_complete
		
		self.remaining_scope = self.total_scope - self.dev_complete
