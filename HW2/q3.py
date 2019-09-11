import numpy as np
import math
value = np.zeros((5, 5))
print(value)
special_stateA = (0, 1)
stateA_ = (4, 1)
special_stateB = (0, 3)
stateB_ = (2, 3)

minimum_change = 0.00001
gamma = 0.9
count = 0
while True:
	count += 1
	# print('count: ', count)
	change = 0
	for i in range(5):
		for j in range(5):
			# (i, j) is the state
			v = 0
			if (i, j) == special_stateA:
				v = 10 + gamma * value[4][1]
			elif (i, j) == special_stateB:
				v = 5 + gamma * value[2][3]
			else:
				# up action
				if i-1 < 0:
					v = -1
				else:
					v = gamma * value[i-1][j]

				# left action
				if j-1 < 0:
					v = max(v, -1)
				else:
					v = max(v, gamma * value[i][j-1])

				#down action
				if i+1 > 4:
					v = max(v, -1)
				else:
					v = max(v, gamma * value[i+1][j])

				# right action
				if j+1 > 4:
					v = max(v, -1)
				else:
					v = max(v, gamma * value[i][j+1])

			change = max(change, abs(v - value[i][j]))
			value[i][j] = v

	if (change < minimum_change):
		break

for i in range(5):
	for j in range(5):
		print(value[i][j] , end="\t")
	print()

# Optimal Policy

policy = np.zeros((5*5, 4))
#  4 columns of the policy are up, left, down, right

for i in range(5):
	for j in range(5):
		m = -math.inf
		if (i-1 >= 0):
			m = max(m, value[i-1, j])
		if (j-1 >= 0):
			m = max(m, value[i, j-1])
		if (i+1 < 5):
			m = max(m, value[i+1, j])
		if (j+1 < 5):
			m = max(m, value[i, j+1])

		if (i-1 >= 0) and value[i-1, j] == m:
			policy[5*i + j][0] = 1
			print(1, end=' ')
		else:
			print(0, end=' ')
		if (j-1 >= 0) and value[i, j-1] == m:
			policy[5*i + j][1] = 1
			print(1, end=' ')
		else:
			print(0, end=' ')

		if (i+1 < 5) and value[i+1, j] == m:
			policy[5*i + j][2] = 1
			print(1, end=' ')
		else:
			print(0, end=' ')

		if (j+1 < 5) and value[i, j+1] == m:
			policy[5*i + j][3] = 1
			print(1, end=' ')
		else:
			print(0, end=' ')
		print()