import random
import numpy as np
import matplotlib.pyplot as plt

# all variables are self explainatory


# actions
LEFT = -1
RIGHT = 1

# initializing Value function
V = [0.5]*7
V[0] = V[6] = 0

def fig1(no_of_episodes, alpha):
	color = ['r', 'g', 'b', 'y']
	c=  0
	for i in range(no_of_episodes):
		state = 3
		while state not in [0, 6]:
			action = random.uniform(0, 1)
			reward = 0
			if action < 0.5:
				action = LEFT
			else:
				action = RIGHT
				if state+action == 6:
					reward = 1
			
			if state+action == 0:
				V[state] = V[state] - alpha*(V[state])
			elif state+action == 6:
				V[state] = V[state] + alpha*(reward - V[state])
			else:
				V[state] = V[state] + alpha*(V[state+action] - V[state])

			state = state + action
		timestep = [0, 1, 9, 99]
		if i in timestep:
			x = [i for i in range(1, 6)]
			print(V)
			plt.plot(x, V[1:6], color[c], label=timestep[c])
			c+=1
	plt.title("TD(0)")
	plt.legend()
	plt.show()

fig1(100, 0.1)