import numpy as np

theta = 0.000001
# V is the random value function
V = np.random.rand(4, 4)
# print(V)
# values of terminal states should be zero
V[0][0] = 0
V[3][3] = 0

gamma = 0.9
reward = -1
count = 0
while True:
	count += 1
	print('Step ', count)
	delta = 0
	for i in range(4):
		for j in range(4):
			# if the current state is the terminal state, then skip it
			if (i, j) == (0, 0) or (i, j) == (3, 3):
				continue
			# variable v is the new value of the current state
			# initially, setting up the max based on the up action. If the next state is out of bounds, then the state does not change. So, the previous value of the  current state will be used to evaluate the new value of the current state. else, the value of the look-ahead state will be used to do the same. Similarly for all the below actions.
			# up action
			if i-1 < 0:
				v = reward + gamma * V[i][j]
			else:
				v = reward + gamma * V[i-1][j]

			# left action
			if j-1 < 0:
				v = max(v, reward + gamma * V[i][j])
			else:
				v = max(v, reward + gamma * V[i][j-1])

			#down action
			if i+1 > 3:
				v = max(v, reward + gamma * V[i][j])
			else:
				v = max(v, reward + gamma * V[i+1][j])

			# right action
			if j+1 > 3:
				v = max(v, reward + gamma * V[i][j])
			else:
				v = max(v, reward + gamma * V[i][j+1])

			delta = max(delta, abs(v - V[i][j]))
			V[i][j] = v;
		print('Intermediate Value function')
		print(V)
		print()
	if (delta < theta):
		break

print('Final Value function')
print(V)
print()