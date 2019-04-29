import numpy as np
import matplotlib.pyplot as plt

def display_activations_functions():

	space = np.arange(-3, 3, 0.02)
	activated = np.where(space <= 0, 0, space)
	plt.plot(space,space, color = "blue");
	plt.plot(space,activated, color = "orange");
	plt.title("Relu")
	plt.axvline(0, color="red", alpha = 0.2);
	plt.axhline(0, color="red", alpha = 0.2);
	plt.show();
	
	
	activated = 1. / (1. + np.exp(-space))
	plt.plot(space,space, color = "blue");
	plt.plot(space,activated, color = "orange");
	plt.title("Sigmoid")
	plt.axvline(0, color="red", alpha = 0.2);
	plt.axhline(0, color="red", alpha = 0.2);
	plt.show();
	
	
	activated = np.log(1+np.exp(space))
	plt.plot(space,space, color = "blue");
	plt.plot(space,activated, color = "orange");
	plt.title("Softplus")
	plt.axvline(0, color="red", alpha = 0.2);
	plt.axhline(0, color="red", alpha = 0.2);
	plt.show();
	
	
	activated = np.tan(space)
	plt.plot(space,space, color = "blue");
	plt.plot(space,activated, color = "orange");
	plt.title("Than")
	plt.axvline(0, color="red", alpha = 0.2);
	plt.axhline(0, color="red", alpha = 0.2);
	plt.show();
	

def test_direction_with_gym_snek(fnc, render=False):
	import gym
	import sneks
	
	env = gym.make("babysnek-raw-16-v1")
	
	res = 0
	
	for _ in range(20):
		obs = env.reset()
		done = False
		if(render):
			env.render()
		while(not done):
			act = fnc(obs)
			obs, r, done, _ = env.step(act)
			if(render):
				env.render()
			res += r
	
	if(res != 20):
		print("Oh no :( you algorithm only got "+str(res))
	else:
		print("Congratulations! Your snake got all fruits!")
