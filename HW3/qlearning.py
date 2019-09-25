import numpy as np
import random

epsilon = 0.3
def q_learning(no_of_episodes, alpha, rewardList):
	Q = np.random.rand(4, 12, 4)
	for i in range(4):
		Q[0, 0, i] = 0
		Q[0, 11, i] = 0
	# print(Q)

	for i in range(no_of_episodes):
		s = (0, 0)
		e = random.uniform(0, 1)
		if (e < epsilon):
			a = random.randint(0, 3)
		else:
			a = np.argmax(Q[s[0], s[1]])

		print("Episode ", i+1)
		while (s != (0, 11)):
			print(s, a)
			if (a == 0):
				reward = -1
				if(s[0]+1 > 3):
					a = np.argmax(Q[s[0], s[1]])
					Q[s[0], s[1], 0] += alpha*(reward + Q[s[0], s[1], a] - Q[s[0], s[1], 0])
				else:
					a = np.argmax(Q[s[0]+1, s[1]])
					Q[s[0], s[1], 0] += alpha*(reward + Q[s[0]+1, s[1], a] - Q[s[0], s[1], 0])
					s = (s[0]+1, s[1])

			elif (a == 1):
				reward = -1
				if(s[1]-1 < 0):
					a = np.argmax(Q[s[0], s[1]])
					Q[s[0], s[1], 1] += alpha*(reward + Q[s[0], s[1], a] - Q[s[0], s[1], 1])
				else:
					a = np.argmax(Q[s[0], s[1]-1])
					Q[s[0], s[1], 1] += alpha*(reward + Q[s[0], s[1]-1, a] - Q[s[0], s[1], 1])
					s = (s[0], s[1]-1)
			elif (a == 2):
				reward = -1
				if(s[0]-1 < 0):
					Q[s[0], s[1], 2] += alpha*(reward)
					a = np.argmax(Q[0, 0])
					Q[s[0], s[1], 2] += alpha*(reward + Q[s[0], s[1], a] - Q[s[0], s[1], 2])

				elif(s[0]-1 < 1):
					reward = -100
					a = np.argmax(Q[0, 0])
					Q[s[0], s[1], 2] += alpha*(reward + Q[0, 0, a] - Q[s[0], s[1], 2])
					s = (0, 0)

				else:
					a = np.argmax(Q[s[0]-1, s[1]])
					Q[s[0], s[1], 2] += alpha*(reward + Q[s[0]-1, s[1], a] - Q[s[0], s[1], 2])
					s = (s[0]-1, s[1])
			else:
				reward = -1
				if (s == (0, 0)):
					reward = -100
					a = np.argmax(Q[0, 0])
					Q[0, 0, 3] += alpha*(reward + Q[0, 0, a] - Q[0, 0, 3])

				elif(s[1]+1 > 11):
					a = np.argmax(Q[s[0], s[1]])
					Q[s[0], s[1], 3] += alpha*(reward + Q[s[0], s[1], a] - Q[s[0], s[1], 3])
				else:
					a = np.argmax(Q[s[0], s[1]+1])
					Q[s[0], s[1], 3] += alpha*(reward + Q[s[0], s[1]+1, a] - Q[s[0], s[1], 3])
					s = (s[0], s[1]+1)

			rewardList = 


def sarsa(no_of_episodes, alpha):
	Q = np.random.rand(4, 12, 4)
	for i in range(4):
		Q[0, 0, i] = 0
		Q[0, 11, i] = 0
	# print(Q)

	for i in range(no_of_episodes):
		s = (0, 0)
		e = random.uniform(0, 1)
		if (e < epsilon):
			a = random.randint(0, 3)
		else:
			a = np.argmax(Q[s[0], s[1]])

		# print("Episode ", i+1)
		while (s != (0, 11)):
			# print(s, a)
			if (a == 0):
				reward = -1
				if(s[0]+1 > 3):
					e = random.uniform(0, 1)
					if (e < epsilon):
						a = random.randint(0, 3)
					else:
						a = np.argmax(Q[s[0], s[1]])
					Q[s[0], s[1], 0] += alpha*(reward + Q[s[0], s[1], a] - Q[s[0], s[1], 0])
				else:
					e = random.uniform(0, 1)
					if (e < epsilon):
						a = random.randint(0, 3)
					else:
						a = np.argmax(Q[s[0]+1, s[1]])
					Q[s[0], s[1], 0] += alpha*(reward + Q[s[0]+1, s[1], a] - Q[s[0], s[1], 0])
					s = (s[0]+1, s[1])

			elif (a == 1):
				reward = -1
				if(s[1]-1 < 0):
					e = random.uniform(0, 1)
					if (e < epsilon):
						a = random.randint(0, 3)
					else:
						a = np.argmax(Q[s[0], s[1]])
					Q[s[0], s[1], 1] += alpha*(reward + Q[s[0], s[1], a] - Q[s[0], s[1], 1])
				else:
					e = random.uniform(0, 1)
					if (e < epsilon):
						a = random.randint(0, 3)
					else:
						a = np.argmax(Q[s[0], s[1]-1])
					Q[s[0], s[1], 1] += alpha*(reward + Q[s[0], s[1]-1, a] - Q[s[0], s[1], 1])
					s = (s[0], s[1]-1)
			elif (a == 2):
				reward = -1
				if(s[0]-1 < 0):
					Q[s[0], s[1], 2] += alpha*(reward)
					e = random.uniform(0, 1)
					if (e < epsilon):
						a = random.randint(0, 3)
					else:
						a = np.argmax(Q[0, 0])
					Q[s[0], s[1], 2] += alpha*(reward + Q[s[0], s[1], a] - Q[s[0], s[1], 2])

				elif(s[0]-1 < 1):
					reward = -100
					e = random.uniform(0, 1)
					if (e < epsilon):
						a = random.randint(0, 3)
					else:
						a = np.argmax(Q[0, 0])
					Q[s[0], s[1], 2] += alpha*(reward + Q[0, 0, a] - Q[s[0], s[1], 2])
					s = (0, 0)

				else:
					e = random.uniform(0, 1)
					if (e < epsilon):
						a = random.randint(0, 3)
					else:
						a = np.argmax(Q[s[0]-1, s[1]])
					Q[s[0], s[1], 2] += alpha*(reward + Q[s[0]-1, s[1], a] - Q[s[0], s[1], 2])
					s = (s[0]-1, s[1])
			else:
				reward = -1
				if (s == (0, 0)):
					reward = -100
					e = random.uniform(0, 1)
					if (e < epsilon):
						a = random.randint(0, 3)
					else:
						a = np.argmax(Q[0, 0])
					Q[0, 0, 3] += alpha*(reward + Q[0, 0, a] - Q[0, 0, 3])					

				elif(s[1]+1 > 11):
					e = random.uniform(0, 1)
					if (e < epsilon):
						a = random.randint(0, 3)
					else:
						a = np.argmax(Q[s[0], s[1]])
					Q[s[0], s[1], 3] += alpha*(reward + Q[s[0], s[1], a] - Q[s[0], s[1], 3])
				else:
					e = random.uniform(0, 1)
					if (e < epsilon):
						a = random.randint(0, 3)
					else:
						a = np.argmax(Q[s[0], s[1]+1])
					Q[s[0], s[1], 3] += alpha*(reward + Q[s[0], s[1]+1, a] - Q[s[0], s[1], 3])
					s = (s[0], s[1]+1)
