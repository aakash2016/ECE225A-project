# %

import random


def dice_roll():
    dice = random.randint(1, 100)
    if dice < 52:
        return False
    else:
        return True


def simulate_casino(total_funds, wager_amount, total_plays):
    """
    :param total_funds: total money in hand the player is starting with
    :param wager_amount: the betting amount each time the player plays
    :param total_plays: the number of times the player bets on this game

    :return:
    """

    funds = []
    playnum = []

    play = 1
    while play <= total_plays:
        # if player wins
        if dice_roll():
            # add money to the fund
            total_funds = total_funds + wager_amount
            funds.append(total_funds)
        # if the house wins
        else:
            # subtract money from the fund
            total_funds = total_funds - wager_amount
            funds.append(total_funds)

        # append and increment the play number
        playnum.append(play)
        play += 1

    # line plot of funds over time
    # plt.plot(playnum, funds)

    # return the remaining fund
    return funds[-1]
