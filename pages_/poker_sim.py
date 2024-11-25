import random
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

import random
from collections import Counter

def change_format(hand):

    list_of_hand = []
    mapping_dict = dict(zip(['Hearts', 'Diamonds', 'Clubs', 'Spades'], 'HDCS'))
    for h in hand:
        x = h.split(" ")
        ans = ''
        if x[0] == '10':
            ans += 'T'
        else:
            ans += x[0]
        ans += mapping_dict[x[2]]
        list_of_hand.append(ans)


    return list_of_hand


# Step 2: Create a function to evaluate hand rankings
def evaluate_hand(hand):
    """
    Evaluates the hand and returns a tuple: (score, high cards).
    Higher scores indicate better hands.
    """
    # Step 1: Define card ranks and suits
    hand = change_format(hand)

    RANKS = "23456789TJQKA"
    SUITS = "CDHS"

    ranks = sorted([RANKS.index(card[0]) for card in hand], reverse=True)
    suits = [card[1] for card in hand]
    rank_counts = Counter(ranks)
    is_flush = len(set(suits)) == 1
    is_straight = len(rank_counts) == 5 and (max(ranks) - min(ranks) == 4)

    # Royal Flush, Straight Flush, and Flush
    if is_straight and is_flush:
        return (9 if max(ranks) == RANKS.index('A') else 8, "Straight Flush")
    elif is_flush:
        return (5, "Flush")
    elif is_straight:
        return (4, "Straight")

    # Four of a Kind, Full House, Three of a Kind, Two Pair, One Pair
    counts = sorted(rank_counts.values(), reverse=True)
    if counts == [4, 1]:
        return (7, "Four of a Kind")
    elif counts == [3, 2]:
        return (6, "Full House")
    elif counts == [3, 1, 1]:
        return (3, "Three of a Kind")
    elif counts == [2, 2, 1]:
        return (2, "Two Pair")
    elif counts == [2, 1, 1, 1]:
        return (1, "One Pair")

    # High Card
    return (0, "High Card")


custom = {"axes.edgecolor": "red", "grid.linestyle": "dashed", "grid.color": "black"}
sns.set_style("darkgrid", rc=custom)

def poker_simulation():

    def calculate_poker_probability(user_hand, num_opponents, num_simulations=1000):
        # Deck initialization
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        deck = [f"{rank} of {suit}" for rank in ranks for suit in suits]

        # Remove user's selected cards from the deck
        for card in user_hand:
            deck.remove(card)

        wins = [0]*num_simulations

        user_score = evaluate_hand(user_hand)

        for _ in range(num_simulations):
            random.shuffle(deck)

            # Simulate opponents' hands
            opponents_hands = [deck[i * 5:(i + 1) * 5] for i in range(num_opponents)]

            # Simulate remaining community cards (Texas Hold'em style)
            # community_cards = deck[num_opponents * 5:num_opponents * 5 + 5]

            # Evaluate opponents' best hands (placeholder)
            # opponent_scores = [random.randint(1, 100) for _ in opponents_hands]

            opponent_scores = [evaluate_hand(h) for h in opponents_hands]

            if user_score[0] > max([s[0] for s in opponent_scores]):
                wins[_] = 1

            # Check if user has the highest score
            # if user_score > max(opponent_scores):
            #     # wins += 1
            #     wins[_] = 1

        # win_probability = (wins / num_simulations) * 100
        return wins, user_score

    # Streamlit app
    st.title("Poker Winning Probability Calculator")
    st.sidebar.header("Select Your Options")

    # User input: Card selection
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [f"{rank} of {suit}" for rank in ranks for suit in suits]

    st.sidebar.subheader("Select 5 Cards")
    user_hand = []
    for i in range(5):
        user_hand.append(st.sidebar.selectbox(f"Card {i + 1}", deck, key=f"card_{i}"))
        # Remove selected card from deck to avoid duplicates
        deck = [card for card in deck if card not in user_hand]

    # User input: Number of opponents
    num_opponents = st.sidebar.slider("Number of Opponents", min_value=1, max_value=8, value=3)
    num_simulations = st.sidebar.slider("Number of Simulations", min_value=10, max_value=1000, value=10)

    # Calculate probability
    if st.sidebar.button("Calculate Probability"):
        st.write("### Your Selected Hand")
        st.write(user_hand)

        st.write("### Number of Opponents")
        st.write(num_opponents)

        with st.spinner("Simulating games..."):
            # l = []
            # for _ in range(num_simulations):
            win_probability_list, user_score = calculate_poker_probability(user_hand, num_opponents, num_simulations= num_simulations)
                # l.append(win_probability)

        st.write("### Probability of Winning")
        st.write(f"Your probability of winning is **{sum(win_probability_list)/len(win_probability_list):.2f}**")
        st.write(f"For User hand: {user_hand}, User score is: {user_score[0]} and Name of the hand is: {user_score[1]}")

        # Display results as a bar chart
        fig, ax = plt.subplots()
        ax.plot(range(1,num_simulations+1), win_probability_list, label=f"Poker Simulation")
        # ax.bar(["Win", "Lose"], [win_probability, 100 - win_probability], color=["green", "red"])
        ax.set_ylabel("Probability")
        ax.set_xlabel("Number of Simulations")
        ax.set_title("Winning Probability Simulation for a selected hand")
        st.pyplot(fig)

    st.sidebar.write("### How to Use")
    st.sidebar.write(
        "1. Select your 5 cards from the dropdown menus.\n"
        "2. Choose the number of opponents.\n"
        "3. Click the 'Calculate Probability' button to see your chances of winning!"
    )


if __name__ == "__main__":
    poker_simulation()