import random
from scipy.stats import norm
import numpy
import matplotlib.pyplot as plt
from math import sqrt, log;

class Bandit:
	def __init__(self, len_action_space=10, epsilon=0.0, step_size=0, initial_value=0.0, ucb_c=0, non_stationary=False):
		self.len_action_space = len_action_space
		self.epsilon = epsilon
		self.step_size = step_size;
		self.initial_value = initial_value;
		# confidence value of ucb
		self.ucb_c = ucb_c;
		self.non_stationary = non_stationary

		self.time = 0
		self.reward_sum = 0
		self.Count = [0]*len_action_space
		self.values = [0.0]*len_action_space
		self.estValues = [initial_value]*len_action_space;
		self.optimalActionCount = 0
		self.values[0] = numpy.random.normal(0, 1)
		Max = 0
		for i in range(1, len_action_space):
			self.values[i] = numpy.random.normal(0, 1);
			if Max < self.values[i]:
				Max = i
		self.optimalAction = Max;

	def bandit(self, action):
		reward = numpy.random.normal(self.values[action], 1);

		if (self.non_stationary):
			Max = 0
			for i in range(1, self.len_action_space):
				self.values[i] = numpy.random.normal(0, 1);
				if Max < self.values[i]:
					Max = i
			self.optimalAction = Max;

		return reward

	def explore(self):
		#choose action
		return random.randint(0, 9)

	def exploit(self):
		#choose action
		argmax = 0
		if self.Count[0] == 0:
			return 0

		Max = self.estValues[0] + self.ucb_c * (sqrt( log(self.time) / self.Count[0]))

		for i in range(1, self.len_action_space):
			if self.Count[i] == 0:
				return i

			tmp = self.estValues[i] + self.ucb_c * (sqrt( log(self.time) / self.Count[i]))
			if tmp > Max:
				Max = tmp
				argmax = i
 
		return argmax;

	def banditTask(self):
		self.time += 1
		epsi = random.uniform(0,1)
		action = -1
		reward = -1
		if epsi < self.epsilon:
			action = self.explore()
		else:
			action = self.exploit()
		if action == self.optimalAction:
			self.optimalActionCount += 1
		reward = self.bandit(action)
		self.reward_sum += reward
		self.Count[action] += 1
		if self.step_size == 0:
			self.estValues[action] = self.estValues[action] + (reward - self.estValues[action])/self.Count[action]
		else:
			self.estValues[action] = self.estValues[action] + (reward - self.estValues[action])*self.step_size;


		return reward;


def q1():
	step_size = [0, 0.1]
	avg_reward = []
	opt_action = []
	n = 10000 #no of steps
	steps = [i for i in range(1, n+1)]
	i = 0
	for ssize in step_size:
		avg_rwd = [0.0] * n
		optimal_action = [0.0] * n
		for i in range(200):
			banditProb = Bandit(step_size=ssize, epsilon=0.1, non_stationary=True)
			for p in range(n):
				avg_rwd[p] += banditProb.banditTask();
				optimal_action[p] += banditProb.optimalActionCount/(p+1)*100;
				if i == 199:
					avg_rwd[p] = avg_rwd[p]/n;
					optimal_action[p] = optimal_action[p] / (200);

		avg_reward.append(avg_rwd)
		opt_action.append(optimal_action)

	a, = plt.plot(steps, avg_reward[0], label='step_size=sample average')
	b, = plt.plot(steps, avg_reward[1], label='step_size=0.1')
	plt.xlabel('Timesteps')
	plt.ylabel('Average Reward')
	plt.legend(handles=[a,b])		
	plt.show()

	a, = plt.plot(steps, opt_action[0], label='e=0.0')
	b, = plt.plot(steps, opt_action[1], label='e=0.01')
	plt.xlabel('Timesteps')
	plt.ylabel('Optimal Action(%)')
	plt.legend(handles=[a,b])		
	plt.show()


def q2_oiv_s():
	epsilon = [0, 0.1]
	iv = [5.0, 0.0]
	opt_action = []
	steps = [i for i in range(1, 1001)]
	i = 0
	for j in range(2):
		optimal_action = [0.0] * 1000
		for i in range(2000):
			banditProb = Bandit(epsilon=epsilon[j], initial_value=iv[j])
			for p in range(1000):
				banditProb.banditTask();
				optimal_action[p] += banditProb.optimalActionCount/(p+1)*100;
				if i == 1999:
					optimal_action[p] = optimal_action[p] / (2000);

		opt_action.append(optimal_action)

	a, = plt.plot(steps, opt_action[0], label='e=0.0')
	b, = plt.plot(steps, opt_action[1], label='e=0.1')
	plt.xlabel('Timesteps')
	plt.ylabel('Optimal Action(%)')
	plt.legend(handles=[a,b])		
	plt.show()


def q2_oiv_ns():
	epsilon = [0, 0.1]
	iv = [5.0, 0.0]
	opt_action = []
	steps = [i for i in range(1, 1001)]
	i = 0
	for j in range(2):
		optimal_action = [0.0] * 1000
		for i in range(2000):
			banditProb = Bandit(epsilon=epsilon[j], initial_value=iv[j], non_stationary=True)
			for p in range(1000):
				banditProb.banditTask();
				optimal_action[p] += banditProb.optimalActionCount/(p+1)*100;
				if i == 1999:
					optimal_action[p] = optimal_action[p] / (2000);

		opt_action.append(optimal_action)

	a, = plt.plot(steps, opt_action[0], label='e=0.0')
	b, = plt.plot(steps, opt_action[1], label='e=0.1')
	plt.xlabel('Timesteps')
	plt.ylabel('Optimal Action(%)')
	plt.legend(handles=[a,b])
	plt.show()


def q4_comparison_s():
	avg_reward = []
	opt_action = []
	
	n = 1000 #no of steps
	steps = [i for i in range(1, n+1)]
	avg_rwd = [0.0]*n;
	optimal_action = [0.0]*n;
	for i in range(2000):
		banditProb = Bandit(epsilon=0.1)
		for p in range(n):
			avg_rwd[p] += banditProb.banditTask();
			optimal_action[p] += banditProb.optimalActionCount/(p+1)*100;
			if i == 1999:
				avg_rwd[p] = avg_rwd[p]/n;
				optimal_action[p] = optimal_action[p] / (2000);

	avg_reward.append(avg_rwd)
	opt_action.append(optimal_action)

	avg_rwd = [0.0]*n;
	optimal_action = [0.0]*n;
	for i in range(2000):
		banditProb = Bandit(initial_value=5.0)
		for p in range(n):
			avg_rwd[p] += banditProb.banditTask();
			optimal_action[p] += banditProb.optimalActionCount/(p+1)*100;
			if i == 1999:
				avg_rwd[p] = avg_rwd[p]/n;
				optimal_action[p] = optimal_action[p] / (2000);

	avg_reward.append(avg_rwd)
	opt_action.append(optimal_action)

	avg_rwd = [0.0]*n;
	optimal_action = [0.0]*n;
	for i in range(2000):
		banditProb = Bandit(ucb_c=2)
		for p in range(n):
			avg_rwd[p] += banditProb.banditTask();
			optimal_action[p] += banditProb.optimalActionCount/(p+1)*100;
			if i == 1999:
				avg_rwd[p] = avg_rwd[p]/n;
				optimal_action[p] = optimal_action[p] / (2000);

	avg_reward.append(avg_rwd)
	opt_action.append(optimal_action)

	a, = plt.plot(steps, avg_reward[0], label='epsilon=0.1')
	b, = plt.plot(steps, avg_reward[1], label='initial_value=5')
	c, = plt.plot(steps, avg_reward[2], label='ucb_c=2')
	plt.xlabel('Timesteps')
	plt.ylabel('Average Reward')
	plt.legend(handles=[a,b,c])
	plt.show()


	a, = plt.plot(steps, opt_action[0], label='epsilon=0.1')
	b, = plt.plot(steps, opt_action[1], label='initial_value=5')
	c, = plt.plot(steps, opt_action[2], label='ucb_c=2')
	plt.xlabel('Timesteps')
	plt.ylabel('Optimal Action(%)')
	plt.legend(handles=[a,b,c])
	plt.show()

def q4_comparison_ns():
	avg_reward = []
	opt_action = []
	
	n = 1000 #no of steps
	steps = [i for i in range(1, n+1)]
	avg_rwd = [0.0]*n;
	optimal_action = [0.0]*n;
	for i in range(2000):
		banditProb = Bandit(epsilon=0.1, non_stationary=True)
		for p in range(n):
			avg_rwd[p] += banditProb.banditTask();
			optimal_action[p] += banditProb.optimalActionCount/(p+1)*100;
			if i == 1999:
				avg_rwd[p] = avg_rwd[p]/n;
				optimal_action[p] = optimal_action[p] / (2000);

	avg_reward.append(avg_rwd)
	opt_action.append(optimal_action)

	avg_rwd = [0.0]*n;
	optimal_action = [0.0]*n;
	for i in range(2000):
		banditProb = Bandit(initial_value=5.0, non_stationary=True)
		for p in range(n):
			avg_rwd[p] += banditProb.banditTask();
			optimal_action[p] += banditProb.optimalActionCount/(p+1)*100;
			if i == 1999:
				avg_rwd[p] = avg_rwd[p]/n;
				optimal_action[p] = optimal_action[p] / (2000);

	avg_reward.append(avg_rwd)
	opt_action.append(optimal_action)

	avg_rwd = [0.0]*n;
	optimal_action = [0.0]*n;
	for i in range(2000):
		banditProb = Bandit(ucb_c=2, non_stationary=True)
		for p in range(n):
			avg_rwd[p] += banditProb.banditTask();
			optimal_action[p] += banditProb.optimalActionCount/(p+1)*100;
			if i == 1999:
				avg_rwd[p] = avg_rwd[p]/n;
				optimal_action[p] = optimal_action[p] / (2000);

	avg_reward.append(avg_rwd)
	opt_action.append(optimal_action)


	a, = plt.plot(steps, avg_reward[0], label='epsilon=0.1')
	b, = plt.plot(steps, avg_reward[1], label='initial_value=5')
	c, = plt.plot(steps, avg_reward[2], label='ucb_c=2')
	plt.xlabel('Timesteps')
	plt.ylabel('Average Reward')
	plt.legend(handles=[a,b,c])
	plt.show()

	a,= plt.plot(steps, opt_action[0], label='epsilon=0.1')
	b, = plt.plot(steps, opt_action[1], label='initial_value=5')
	c, = plt.plot(steps, opt_action[2], label='ucb_c=2')
	plt.xlabel('Timesteps')
	plt.ylabel('Optimal Action(%)')
	plt.legend(handles=[a,b,c])
	plt.show()


q1()
q2_oiv_s()
q2_oiv_ns()
q4_comparison_s()
q4_comparison_ns()