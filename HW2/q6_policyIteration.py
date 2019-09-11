import numpy as np
import math

policy = []

n = 4
# police is initialized
for i in range(n):
	row = []
	for j in range(n):
		row.append([1, 1, 1, 1])
	policy.append(row)

# setting the policy of the terminal state
policy[0][0] = [0 for i in range(n)]
policy[3][3] = [0 for i in range(n)]


theta = 0.00001
gamma = 0.9

# actions for a given state are: 
# (-1,0) -> up
# (0,-1) -> left
# (1,0) -> down
# (0,1) -> right

action = [(-1, 0), (0, -1), (1, 0), (0, 1)]
policy_stable = False
reward = -1
count = 0
while not policy_stable:
	V = np.zeros((n, n))
	count += 1
	print('Step ', count)
	# Evaluating Policy
	while True:
		delta = 0
		# below 2 for loops define for each state, which is a cell in the grid
		for i in range(n):
			for j in range(n):
				# variable v is the new value of the current state
				v = 0

				s = sum(policy[i][j])
				# if the state is a terminal state, do nothing
				if (i, j) == (0, 0) or (i, j) == (3, 3):
					continue
				
				# in each of the below functions, the if condition checks if the next state is out of bounds or not. If it is out of bounds, then the state remains unchanged, else the state changes and the value function is changed based on the next state

				# up action
				if i-1 < 0:
					v += (policy[i][j][0]/s) * (reward + gamma * V[i][j])
				else:
					v += (policy[i][j][0]/s) * (reward + gamma * V[i-1][j])

				# left action
				if j-1 < 0:
					v += (policy[i][j][1]/s) * (reward + gamma * V[i][j])
				else:
					v += (policy[i][j][1]/s) * (reward + gamma * V[i][j-1])

				#down action
				if i+1 > 3:
					v += (policy[i][j][2]/s) * (reward + gamma * V[i][j])
				else:
					v += (policy[i][j][2]/s) * (reward + gamma * V[i+1][j])

				# right action
				if j+1 > 3:
					v += (policy[i][j][3]/s) * (reward + gamma * V[i][j])
				else:
					v += (policy[i][j][3]/s) * (reward + gamma * V[i][j+1])

				delta = max(delta, abs(v - V[i][j]))
				V[i][j] = v;

		if (delta < theta):
			break

	#intermediate value function
	print("Value Function\n\t", end ='')
	for i in range(n):
		for j in range(n):
			print(V[i][j], end='\t\t')
		print()
	print()
	

	# Policy Improvement
	policy_stable = True
	for i in range(n):
		for j in range(n):
			# checking if the current state is the terminal state
			if (i, j) == (0, 0) or (i, j) == (3, 3):
				continue

			# print('state ', (i,j))
			old_policy = [policy[i][j][k] for k in range(4)]
			# print('old_policy ', old_policy)
			
			# now finding the value of the current state based on different actions and respectively their corresponding next states defined by (next_i, next_j)
			x = []
			for k in range(4):
				next_i = i + action[k][0]
				next_j = j + action[k][1]

				if (next_i < 0 or next_j > 3 or next_i > 3 or next_j < 0):
					x += [reward + gamma * V[i][j]]
				else:
					x += [reward + gamma * V[next_i][next_j]]

			# finding the max value of all the actions
			m = max(x)

			# then marking all those actions 1 which has maximum value
			for k in range(4):
				if x[k] == m:
					policy[i][j][k] = 1
				else:
					policy[i][j][k] = 0


			# print('new_policy ', policy[i][j])
			# checking if the new policy is same as the old policy or not
			if old_policy != policy[i][j]:
				policy_stable = False


	# intermediate policy
	print("Policy")
	for i in range(4):
		for j in range(4):
			print(policy[i][j], end = ' ')
		print()
	print()


print("Final Value and Policy Functions")
print("Policy")
for i in range(n):
	for j in range(n):
		print(V[i][j], end=' ')
	print()

print()

for i in range(4):
	for j in range(4):
		print(policy[i][j], end = ' ')
	print()