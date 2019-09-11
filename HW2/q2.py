import numpy as np

n = 5
# nStates define the number of states in the MDP
nStates = n*n
# V is the value function. Initially, it is Zero for all states
V = np.zeros(nStates)
# R is the Expected rewards for all states.
R = np.zeros(nStates)
# P is the initial policy
P = np.zeros((nStates, nStates))
# I is the Identity Matrix which is used to solve the Bellman Equations
I = np.identity(nStates, dtype=float)

# pi = 0.25 means for every action in each state, they are all equi-probable, ie, they all occur with probability 0.25
pi = 0.25
# reward variable defines the reward of -1 whenever an action takes the agent out of bounds
reward = -1
# gamma is the discount factor
gamma = 0.9

for i in range(n):
	for j in range(n):
		if (i == 0) or (i == n-1):
			R[i*n + j] += pi * reward
		if (j == 0) or (j == n-1):
			R[i*n + j] += pi * reward

# R[1] is the expected reward of state A (0, 1)
R[1] = 10
# R[3] is the expected reward of state B (0, 4)
R[3] = 5

# action is the set of actions which the agent can take in a given state (i, j). (-1, 0) -> up action, (-1, 0) -> left action, (-1, 0) -> down action, (-1, 0) -> right action
action = [(-1, 0), (0, -1), (1, 0), (0, 1)]
for i in range(n):
	for j in range(n):
		# current state is (i, j)
		# below condition checks if the given state is the special state A (0, 1) which gives a reward of 10 and the next state is always (4, 1)
		if (i == 0) and (j == 1):
			next_i = 4
			next_j = 1
			P[i*n + j][next_i*n + next_j] = 1
			continue
		# below condition checks if the given state is the special state B (0, 4) which gives a reward of 5 and the next state is always (2, 4)
		elif (i == 0) and (j == 4):
			next_i = 2
			next_j = 4
			P[i*n + j][next_i*n + next_j] = 1
			continue
		# if the current state is not one of the special states
		for k in range(4):
			next_i = i + action[k][0]
			next_j = j + action[k][1]
			# above two gives the next state
			if (next_i >= 0) and (next_i < 4) and (next_j >= 0) and (next_j < 4):
				# below is the probability of state transition from state (i, j) to state (next_i, next_j) which is pi
				P[i*n + j][next_i*n + next_j] += pi

# below function solves the equation v = matrix multiplication of inverse of (I - gamma*P) and R
V = np.linalg.solve(I - gamma * P, R)
for i in range(n):
	for j in range(n):
		print(V[i*n + j], end=' ')
	print()