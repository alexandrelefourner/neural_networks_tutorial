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
	
	