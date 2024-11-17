import streamlit as st
import random
import itertools
import matplotlib.pyplot as plt

def calculate_poker_probability(user_hand, num_opponents, num_simulations=1000):
    # Deck initialization
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [f"{rank} of {suit}" for rank in ranks for suit in suits]

    # Remove user's selected cards from the deck
    for card in user_hand:
        deck.remove(card)

    wins = 0

    for _ in range(num_simulations):
        random.shuffle(deck)

        # Simulate opponents' hands
        opponents_hands = [deck[i * 5:(i + 1) * 5] for i in range(num_opponents)]

        # Simulate remaining community cards (Texas Hold'em style)
        community_cards = deck[num_opponents * 5:num_opponents * 5 + 5]

        # User's best hand logic (placeholder)
        user_score = random.randint(1, 100)  # Replace with real poker hand evaluation logic

        # Evaluate opponents' best hands (placeholder)
        opponent_scores = [random.randint(1, 100) for _ in opponents_hands]

        # Check if user has the highest score
        if user_score > max(opponent_scores):
            wins += 1

    win_probability = (wins / num_simulations) * 100
    return win_probability

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

# Calculate probability
if st.sidebar.button("Calculate Probability"):
    st.write("### Your Selected Hand")
    st.write(user_hand)

    st.write("### Number of Opponents")
    st.write(num_opponents)

    with st.spinner("Simulating games..."):
        win_probability = calculate_poker_probability(user_hand, num_opponents)

    st.write("### Probability of Winning")
    st.write(f"Your probability of winning is **{win_probability:.2f}%**")

    # Display results as a bar chart
    fig, ax = plt.subplots()
    ax.bar(["Win", "Lose"], [win_probability, 100 - win_probability], color=["green", "red"])
    ax.set_ylabel("Probability (%)")
    ax.set_title("Winning Probability")
    st.pyplot(fig)

st.sidebar.write("### How to Use")
st.sidebar.write(
    "1. Select your 5 cards from the dropdown menus.\n"
    "2. Choose the number of opponents.\n"
    "3. Click the 'Calculate Probability' button to see your chances of winning!"
)
