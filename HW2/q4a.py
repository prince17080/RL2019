import numpy as np
import math
# inititalisation  of Value Function and Policy
# V = np.zeros((6, 6))
policy = []

# police is initialized
for i in range(4):
	row = []
	for j in range(4):
		row.append([1, 1, 1, 1])
	policy.append(row)

policy[0][0] = [0,0,0,0]
policy[3][3] = [0,0,0,0]


theta = 0.0001
gamma = 1
action = [(-1, 0), (0, -1), (1, 0), (0, 1)]
policy_stable = False
count = 0

while not policy_stable:
	V = np.zeros((6, 6))
	count += 1
	print('Step ', count)
	# Evaluating Policy
	while True:
		delta = 0
		# below 2 for loops define for each state, which is a cell in the grid
		for i in range(1, 5):
			for j in range(1, 5):
				v = 0
				# if the state is a terminal state, do nothing
				if (i == 1 and j == 1) or (i == 4 and j == 4):
					continue
				# Sum is used to find the probability, pi(a | s)
				Sum = sum(policy[i-1][j-1])
				# below for loop defines for each action in the action space of the  current state, ie, actionTaken
				# action space: k = 0: up action
				#				k = 1: left action
				# 				k = 2: down action
				#				k = 3: right action

				for k in range(4):
					# actionTaken can take values 0 or 1. 0 if the actionTaken == 0, then it is not in the action space of the the current state 
					actionTaken = policy[i-1][j-1][k]
					# prob is the probability of taking action 'actionTaken' given the current state is (i, j)
					action_prob = actionTaken/Sum
					# below if statement checks if the look-ahead state is within the bounds or not. if not, then the state is not changed
					if (i+action[k][0] > 0) and (i+action[k][0] < 5) and (j+action[k][1] > 0) and (j+action[k][1] < 5):
						# if the look-ahead state is the terminal state
						if (i+action[k][0] == 1 and j+action[k][1] == 1) or (i+action[k][0] == 4 and j+action[k][1] == 4):
							reward = 0
						else:
							reward = -1
						v += action_prob * (reward + gamma * V[i+action[k][0]][j+action[k][1]])
					else:
						reward = -1
						v += action_prob * (reward)# + gamma * V[i][j])
				delta = max(delta, abs(v - V[i][j]))
				V[i][j] = round(v, 4)

		if (delta < theta):
			break

	print("Value Function\n\t", end ='')
	for i in range(1, 5):
		for j in range(1,5):
			print(V[i][j], end='\t\t')
		print()
	print()
	

	policy_stable = True
	for i in range(1, 5):
		for j in range(1, 5):
			if i == 1 and j == 1 or i == 4 and j == 4:
				continue
			old_policy = [policy[i-1][j-1][k] for k in range(4)]

			m = -math.inf
			for k in range(4):
				if (i+action[k][0] > 0) and (i+action[k][0] < 5) and (j+action[k][1] > 0) and (j+action[k][1] < 5):
					m = max(m, V[i+action[k][0]][j+action[k][1]])
			
			for k in range(4):
				if (i+action[k][0] >= 1) and (i+action[k][0] < 5) and (j+action[k][1] >= 1) and (j+action[k][1] < 5) and (V[i+action[k][0]][j+action[k][1]] == m):
					policy[i-1][j-1][k] = 1
				else:
					policy[i-1][j-1][k] = 0

			if old_policy != policy[i-1][j-1]:
				policy_stable = False

	print("Policy")
	for i in range(4):
		for j in range(4):
			print(policy[i][j], end = ' ')
		print()
	print()


for i in range(1, 5):
	for j in range(1, 5):
		print(V[i][j], end=' ')
	print()

print()

for i in range(4):
	for j in range(4):
		print(policy[i][j], end = ' ')
	print()