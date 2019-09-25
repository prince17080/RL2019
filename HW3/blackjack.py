import random
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# all variables are self-explainiable

# actions
HIT = 0
STICK = 1

# game conditions
SAFE = 2
BUST = 3
NATURAL = 4

# below actions initializes the player state
def initial_state():
	dealers_showing_card = min(random.randint(1, 13), 10)
	player_sum = 0
	player_has_usable_ace = False

	while player_sum < 12:
		card = min(random.randint(1, 13), 10)
		if card == 1:
			card = 11
			player_has_usable_ace = True

		player_sum += card
		if player_sum > 21 and player_has_usable_ace:
			player_sum -= 10

	return dealers_showing_card, player_sum, player_has_usable_ace

# below actions initializes the dealer state
def dealers_initial_state(card1):
	dealers_card_1 = card1
	dealers_card_2 = min(random.randint(1, 13), 10)

	dealer_has_usable_ace = False
	if 1 in (dealers_card_1, dealers_card_2):
		dealer_has_usable_ace = True

	dealer_sum = dealers_card_1 + dealers_card_2
	while dealer_sum < 12:
		card = min(random.randint(1, 13), 10)
		if card == 1:
			card = 11
			dealer_has_usable_ace = True

		dealer_sum += card
		if dealer_sum > 21 and dealer_has_usable_ace:
			dealer_sum -= 10

	return dealer_sum, dealer_has_usable_ace

# below is the player policy
def player_policy(player_sum):
	if player_sum < 20:
		action = HIT
	else:
		action = STICK
	return action

# below is the dealer policy
def dealer_policy(dealer_sum):
	if dealer_sum < 17:
		action = HIT
	else:
		action = STICK
	return action


# below function takes the action and returns the next state.
def next_state(player_sum, usable_ace, action):
	if action == HIT:
		ace_count = 0
		if usable_ace:
			ace_count += 1
		# new card
		card = min(random.randint(1, 13), 10)
		if card == 1:
			card = 11
			usable_ace = True
			ace_count += 1

		player_sum += + card
		if (player_sum > 21) and usable_ace:
			player_sum -= 10
			if ace_count == 1:
				usable_ace = False

		if player_sum > 21:
			# player bust
			return BUST, 0, 0

		return SAFE, player_sum, usable_ace
	return STICK, 0, 0

def get_episode():
	reward = 0
	episode = []
	player_condition = -1
	dealer_condition = -1
	dealers_card_1, player_sum, usable_ace = initial_state()

	while True:
		action = player_policy(player_sum)
		# print(dealers_card_1, player_sum, usable_ace, action)
		episode.append((dealers_card_1, player_sum, usable_ace, action))
		player_condition, player_sum, usable_ace = next_state(player_sum, usable_ace, action)

		if player_sum == 21:
			player_condition = NATURAL
			break
		if player_condition in [BUST, STICK]:
			break
		

	if player_condition == BUST:
		reward = -1
		return reward, episode

	dealer_sum, usable_ace = dealers_initial_state(dealers_card_1)
	while True:
		if dealer_sum == 21:
			# natural for dealer
			dealer_condition = NATURAL
			break

		action = dealer_policy(dealer_sum)
		dealer_condition, dealer_sum, usable_ace = next_state(dealer_sum, usable_ace, action)
		if dealer_condition in [BUST, STICK]:
			break

	if dealer_condition == BUST:
		reward = 1
		return reward, episode

	if dealer_sum == player_sum:
		reward = 0
	elif dealer_sum < player_sum:
		reward = 1
	else:
		reward = -1

	return reward, episode


def fig1(no_of_episodes):
	value_usable_ace = np.zeros((10, 10))
	count_usable_ace = np.ones((10, 10))
	value_not_usable_ace = np.zeros((10, 10))
	count_not_usable_ace = np.ones((10, 10))
	no_of_episodes = 10000

	for i in range(no_of_episodes):
		reward, episode = get_episode()
		for dealers_card, player_sum, usable_ace, action in episode:
			player_sum = player_sum - 12
			dealers_card = dealers_card - 1
			if usable_ace:
				value_usable_ace[player_sum, dealers_card] += reward
				count_usable_ace[player_sum, dealers_card] += 1
			else:
				value_not_usable_ace[player_sum, dealers_card] += reward
				count_not_usable_ace[player_sum, dealers_card] += 1
	# plt.figure(1)
	# ax = plt.axes(projection="3d")
	# x_line = []
	# y_line = []
	# z_line = []
	# for i in range(10):
	# 	for j in range(10):
	# 		x_line.append(i+12)
	# 		y_line.append(j+1)
	# 		z_line.append(value_usable_ace[i,j]/count_usable_ace[i,j])
	# ax.scatter3D(x_line, y_line, z_line, c=z_line, cmap='hsv');
	

	plt.figure(2)
	ax = plt.axes(projection="3d")
	x_line = []
	y_line = []
	z_line = []
	for i in range(10):
		for j in range(10):
			x_line.append(i+12)
			y_line.append(j+1)
			z_line.append(value_not_usable_ace[i,j]/count_not_usable_ace[i,j])
	ax.scatter3D(x_line, y_line, z_line, c=z_line, cmap='hsv');

	plt.show()

def fig2(no_of_episodes):
	pi1 = np.zeros((10, 10))
	pi2 = np.zeros((10, 10))
	for i in range(10):
		for j in range(10):
			pi1[i, j] = random.randint(0, 1)
			pi2[i, j] = random.randint(0, 1)

	q_usable_ace = np.zeros((10, 10, 2))
	count_usable_ace = np.ones((10, 10, 2))
	q_not_usable_ace = np.zeros((10, 10, 2))
	count_not_usable_ace = np.ones((10, 10, 2))

	value_usable_ace = np.zeros((10, 10))
	value_not_usable_ace = np.zeros((10, 10))

	for i in range(no_of_episodes):
		reward, episode = get_episode()

		for dealers_card, player_sum, usable_ace, action in episode:
			player_sum = player_sum - 12
			dealers_card = dealers_card - 1
			if usable_ace:
				count_usable_ace[player_sum, dealers_card, action] += 1
				q = q_usable_ace[player_sum, dealers_card, action] 
				c = count_usable_ace[player_sum, dealers_card, action]
				q_usable_ace[player_sum, dealers_card, action] += (reward - q)/c
				
				if q_usable_ace[player_sum, dealers_card, 1] > q_usable_ace[player_sum, dealers_card, 0]:
					pi1[player_sum, dealers_card] = 1
				else:
					pi1[player_sum, dealers_card] = 0
				value_usable_ace[player_sum, dealers_card] = max(q_usable_ace[player_sum, dealers_card, 0], q_usable_ace[player_sum, dealers_card, 1])
			else:
				count_not_usable_ace[player_sum, dealers_card, action] += 1
				q = q_not_usable_ace[player_sum, dealers_card, action] 
				c = count_not_usable_ace[player_sum, dealers_card, action]
				q_not_usable_ace[player_sum, dealers_card, action] += (reward-q)/c
				
				if q_not_usable_ace[player_sum, dealers_card, 1] > q_not_usable_ace[player_sum, dealers_card, 0]:
					pi2[player_sum, dealers_card] = 1
				else:
					pi2[player_sum, dealers_card] = 0
				value_not_usable_ace[player_sum, dealers_card] = max(q_not_usable_ace[player_sum, dealers_card, 0] , q_not_usable_ace[player_sum, dealers_card, 1])

	plt.figure(1)
	ax = plt.axes(projection="3d")
	# x_line = []
	# y_line = []
	# z_line = []
	# for i in range(10):
	# 	for j in range(10):
	# 		x_line.append(i+12)
	# 		y_line.append(j+1)
	# 		z_line.append(value_usable_ace[i,j])
	# ax.scatter3D(x_line, y_line, z_line, c=z_line, cmap='hsv');
	

	# plt.figure(2)
	x_line = []
	y_line = []
	z_line = []
	for i in range(10):
		for j in range(10):
			x_line.append(i+12)
			y_line.append(j+1)
			z_line.append(value_not_usable_ace[i,j])
	ax.scatter3D(x_line, y_line, z_line, c=z_line, cmap='hsv');

	# plt.figure(3)
	# x_line = []
	# y_line = []
	# z_line = []
	# for i in range(10):
	# 	for j in range(10):
	# 		x_line.append(i+12)
	# 		y_line.append(j+1)
	# 		z_line.append(pi1[i, j])
	# ax.scatter3D(x_line, y_line, z_line, c=z_line, cmap='hsv');


	plt.show()

# fig1(10000)
fig2(500000)