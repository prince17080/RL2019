import numpy as np

n = 5
nStates = n*n
V = np.zeros(nStates)
R = np.zeros(nStates)
P = np.zeros((nStates, nStates))
I = np.identity(nStates, dtype=float)

pi = 0.25
reward = -1
gamma = 0.9

for i in range(n):
	for j in range(n):
		if (i == 0) or (i == n-1):
			R[i*n + j] += pi * reward
		if (j == 0) or (j == n-1):
			R[i*n + j] += pi * reward

R[1] = 10
R[3] = 5

action = [(-1, 0), (0, -1), (1, 0), (0, 1)]
for i in range(n):
	for j in range(n):
		if (i == 0) and (j == 1):
			next_i = 4
			next_j = 1
			P[i*n + j][next_i*n + next_j] += gamma
			continue
		elif (i == 0) and (j == 4):
			next_i = 2
			next_j = 4
			P[i*n + j][next_i*n + next_j] += gamma
			continue

		for k in range(4):
			next_i = i + action[k][0]
			next_j = j + action[k][1]
			if (next_i >= 0) and (next_i < 4) and (next_j >= 0) and (next_j < 4):
				# print(i, j, "->", next_i, next_j)
				P[i*n + j][next_i*n + next_j] += (gamma * pi)

# print(P)
print(R)
V = np.linalg.solve(I - P, R)
for i in range(n):
	for j in range(n):
		print(V[i*n + j], end=' ')
	print()
