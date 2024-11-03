# %

import random


def monty_hall_simulation(num_trials, switch):
    wins = 0
    win_history = []

    for trial in range(1, num_trials + 1):
        doors = ['goat', 'goat', 'car']
        random.shuffle(doors)

        # player's initial choice
        player_choice = random.randint(0, 2)

        # host opens a door with a goat that the player did not pick
        host_choice = next(i for i in range(3) if i != player_choice and doors[i] == 'goat')

        # player's decision to switch or stay
        if switch:
            player_choice = next(i for i in range(3) if i != player_choice and i != host_choice)

        # Record a win if the player chose the car
        if doors[player_choice] == 'car':
            wins += 1

        win_history.append(wins / trial)

    return wins, win_history
