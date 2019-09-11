import numpy as np

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
	print('count: ', count)
	change = 0
	for i in range(5):
		for j in range(5):
			# (i, j) is the state
			v = 0
			if i == 0 and j == 1:
				v = 10 + gamma * value[4][1]
			elif i == 0 and j == 3:
				v = 5 + gamma * value[2][3]
			else:
				# top action
				if i-1 < 0:
					v += 0.25 * (-1)
				else:
					v += 0.25 * (gamma * value[i-1][j])

				# left action
				if j-1 < 0:
					v += 0.25 * (-1)
				else:
					v += 0.25 * (gamma * value[i][j-1])

				#down action
				if i+1 > 4:
					v += 0.25 * (-1)
				else:
					v += 0.25 * (gamma * value[i+1][j])

				# right action
				if j+1 > 4:
					v += 0.25 * (-1)
				else:
					v += 0.25 * (gamma * value[i][j+1])

			change = max(change, abs(v - value[i][j]))
			value[i][j] = v

	if (change < minimum_change):
		break

for i in range(5):
	for j in range(5):
		print(value[i][j] , end="\t")
	print()