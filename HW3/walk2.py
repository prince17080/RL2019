import random
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

LEFT = -1
RIGHT = 1

true_V = [i/6 for i in range(7)]
true_V[6] = 0


def monteCarlo(no_of_episodes, alpha, mc_rms):
	V = [0.5 for i in range(7)]
	V[0] = V[6] = 0
	o_rms = 0
	for i in range(no_of_episodes):
		n_rms = 0
		state = 3
		episode = []
		while state not in [0, 6]:
			episode.append(state)
			action = random.uniform(0, 1)
			if action < 0.5:
				action = LEFT
			else:
				action = RIGHT
			state = state + action

		reward = 0
		if episode[-1] == 5:
			reward = 1

		for state in episode:
			V[state] = V[state] + alpha*(reward - V[state])
			state = state + action

		for state in range(1, 6):
			n_rms += ((V[state] - true_V[state])**2)/5
		n_rms = sqrt(n_rms)
		mc_rms[i] = o_rms + (n_rms - o_rms)/(i+1)
		o_rms = n_rms


def td0(no_of_episodes, alpha, td_rms):
	V = [0.5 for i in range(7)]
	V[0] = V[6] = 0
	o_rms = 0
	for i in range(no_of_episodes):
		n_rms = 0
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

		for state in range(1, 6):
			n_rms += ((V[state] - true_V[state])**2)/5
		n_rms = sqrt(n_rms)
		td_rms[i] = o_rms + (n_rms - o_rms)/(i+1)
		o_rms = n_rms

def fig2():
	x = [i for i in range(100)]
	td_rms = np.zeros(100)
	td0(100, 0.05, td_rms)
	plt.plot(x, td_rms, label='td,0.05')

	td_rms = np.zeros(100)
	td0(100, 0.1, td_rms)
	plt.plot(x, td_rms, label='td,0.1')

	td_rms = np.zeros(100)
	td0(100, 0.15, td_rms)
	plt.plot(x, td_rms, label='td,0.15')

	mc_rms = np.zeros(100)
	monteCarlo(100, 0.01, mc_rms)
	plt.plot(x, mc_rms, label='mc,0.01')

	mc_rms = np.zeros(100)
	monteCarlo(100, 0.02, mc_rms)
	plt.plot(x, mc_rms, label='mc,0.02')

	mc_rms = np.zeros(100)
	monteCarlo(100, 0.03, mc_rms)
	plt.plot(x, mc_rms, label='mc,0.03')

	plt.title("RMS")
	plt.legend()
	plt.show()

fig2()
