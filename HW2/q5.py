import numpy as np
import math
# inititalisation  of Value Function and Policy

n = 20

V = np.zeros((n+2, n+2))
policy = []

for i in range(n):
	row = []
	for j in range(n):
		row.append([0, 0, 0, 0])
	policy.append(row)


theta = 0.00001
reward = -1
gamma = 0.9
actionSpace = [(-1, 0), (0, -1), (1, 0), (0, 1)]
policy_stable = False
count = 0

while not policy_stable:
	count += 1
	print('Step ', count)
	while True:
		delta = 0
		for i in range(1, 5):
			for j in range(1, 5):
				v = 0
				if (i == 1 and j == 1) or (i == 4 and j == 4):
					continue
				
				Sum = sum(policy[i-1][j-1])
				for k in range(4):
					action = policy[i-1][j-1][k]
					# if (i+actionSpace[k][0] == 1 and j+actionSpace[k][1] == 1) or (i+actionSpace[k][0] == 4 and j+actionSpace[k][1] == 4):
					# 	v += (action/Sum) * gamma * V[i+actionSpace[k][0]][j+actionSpace[k][1]]
					# else:
					v += (action/Sum) * (reward + gamma * V[i+actionSpace[k][0]][j+actionSpace[k][1]])
				delta = max(delta, abs(v - V[i][j]))
				V[i][j] = v

		if (delta < theta):
			break

	print("Value Function")
	for i in range(1, 5):
		for j in range(1,5):
			print(V[i][j], end='\t')
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
				if (i+actionSpace[k][0] >= 1) and (i+actionSpace[k][0] < 5) and (j+actionSpace[k][1] >= 1) and (j+actionSpace[k][1] < 5):
					m = max(m, V[i+actionSpace[k][0]][j+actionSpace[k][1]])
			for k in range(4):
				if (V[i+actionSpace[k][0]][j+actionSpace[k][1]] == m) and (i+actionSpace[k][0] >= 1) and (i+actionSpace[k][0] < 5) and (j+actionSpace[k][1] >= 1) and (j+actionSpace[k][1] < 5):
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