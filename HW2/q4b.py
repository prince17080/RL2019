import numpy as np

theta = 0.0001
V = np.random.rand(4, 4) * 10
# print(V)
V[0][0] = 0
V[3][3] = 0

gamma = 1
reward = -1
while True:
	delta = 0
	for i in range(4):
		for j in range(4):
			if (i, j) == (0, 0) or (i, j) == (3, 3):
				v = 0
			else:
				# up action
				reward = -1
				if i-1 < 0:
					v = reward
				else:
					if (i == 1 and j == 0):
						reward = 0
					v = reward + gamma * V[i-1][j]

				# left action
				if j-1 < 0:
					v = max(v, -1)
				else:
					if (i == 0 and j == 1):
						reward = 0
					v = max(v, reward + gamma * V[i][j-1])

				#down action
				if i+1 > 3:
					v = max(v, -1)
				else:
					if (i == 2 and j == 3):
						reward = 0
					v = max(v, reward + gamma * V[i+1][j])

				# right action
				if j+1 > 3:
					v = max(v, -1)
				else:
					if (i == 3 and j == 2):
						reward = 0
					v = max(v, reward + gamma * V[i][j+1])

			delta = max(delta, abs(v - V[i][j]))
			V[i][j] = v;
	if (delta < theta):
		break
	print(V)
	print()

print(V)