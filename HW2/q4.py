import numpy as np
import math

# value is the initial value function
value = np.zeros((5, 5))

# below are the 2 speacial states as given in the question statement and their transition to the respective next states by choosing any of the given actions
special_stateA = (0, 1)
stateA_ = (4, 1)

special_stateB = (0, 3)
stateB_ = (2, 3)

# theta is the parameter of the algorithm to stop the iteration 
theta = 0.01
# gamma is the discount factor
gamma = 0.9
while True:
	delta = 0
	for i in range(5):
		for j in range(5):
			# (i, j) is the current state
			# variable v is the new value of the current state
			
			v = 0

			# if the current state is one of the speacial states then its value is as shown below, since choosing any action in these states goes to their respective next state
			if (i, j) == special_stateA:
				v = 10 + gamma * value[4][1]
			elif (i, j) == special_stateB:
				v = 5 + gamma * value[2][3]
			else:
				# initially, setting up the max based on the up action. If the next state is out of bounds,then the state does not change. Else, reward is zero. Similarly, for all the below actions
				# up action
				if i-1 < 0:
					v = -1 + gamma * value[i][j]
				else:
					v = gamma * value[i-1][j]

				# left action
				if j-1 < 0:
					v = max(v, -1 + gamma * value[i][j])
				else:
					v = max(v, gamma * value[i][j-1])

				#down action
				if i+1 > 4:
					v = max(v, -1 + gamma * value[i][j])
				else:
					v = max(v, gamma * value[i+1][j])

				# right action
				if j+1 > 4:
					v = max(v, -1 + gamma * value[i][j])
				else:
					v = max(v, gamma * value[i][j+1])


			delta = max(delta, abs(v - value[i][j]))
			value[i][j] = round(v, 2)

	if (delta < theta):
		break

for i in range(5):
	for j in range(5):
		print(value[i][j] , end="\t")
	print()

# Optimal Policy
policy = np.zeros((5*5, 4))
#  4 columns of the policy are up, left, down, right

print('State\tProbabilty Distribution of Actions\n     \tup\tleft\tdown\tright')
for i in range(5):
	for j in range(5):
		print('('+str(i), str(j)+'): \t', end='')
		m = -math.inf
		# first, finding the maximmum action values
		if (i-1 >= 0):
			m = max(m, value[i-1, j])
		if (j-1 >= 0):
			m = max(m, value[i, j-1])
		if (i+1 < 5):
			m = max(m, value[i+1, j])
		if (j+1 < 5):
			m = max(m, value[i, j+1])

		# second, finding the actions with the maximum value and marking them as 1
		if (i-1 >= 0) and value[i-1, j] == m:
			policy[5*i + j][0] = 1
			print(1, end='\t')
		else:
			print(0, end='\t')

		if (j-1 >= 0) and value[i, j-1] == m:
			policy[5*i + j][1] = 1
			print(1, end='\t')
		else:
			print(0, end='\t')

		if (i+1 < 5) and value[i+1, j] == m:
			policy[5*i + j][2] = 1
			print(1, end='\t')
		else:
			print(0, end='\t')

		if (j+1 < 5) and value[i, j+1] == m:
			policy[5*i + j][3] = 1
			print(1, end='\t')
		else:
			print(0, end='\t')
		print()