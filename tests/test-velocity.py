from velocity import Velocity

def test_should_have_model_velocity():
	velocity = Velocity(model_velocity = 5)
	assert velocity.model == 5