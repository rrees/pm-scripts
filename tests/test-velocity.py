from velocity import Velocity

def test_should_have_model_velocity():
	velocity = Velocity(model_velocity = 5)
	assert velocity.model == 5

def test_should_have_low_velocity():
	velocity = Velocity(low_velocity = 2)
	assert velocity.low == 2

def test_should_have_high_velocity():
	assert Velocity(high_velocity = 16).high == 16

def test_should_have_yesterdays_velocity():
	assert Velocity(yesterdays_velocity = 6).yesterday == 6