"""
    "Underwriting Profits: The Hidden Dynamics of Insurance Success"
"""

import numpy as np
import matplotlib.pyplot as plt

def simulate_insurance(num_policies, num_years):
    """
    Let's consider a simplified car insurance scenario:
        The insurance company charges an annual premium of $1000 per policy.
        Based on historical data, there's a 5% chance of an accident claim in a year.
        If there's a claim, the average payout is $10,000.
    """

    premiums = 1000 * num_policies * num_years
    claims = np.random.binomial(num_policies * num_years, 0.05) * 10000
    profit = premiums - claims
    return profit

# Run simulation multiple times
num_simulations = 100000
results = [simulate_insurance(100, 1) for _ in range(num_simulations)]
print(results)

# Analyze results
average_profit = np.mean(results)
profit_probability = np.sum(np.array(results) > 0) / num_simulations

print(f"Average annual profit: ${average_profit:.2f}")
print(f"Probability of making a profit: {profit_probability:.2%}")

# Plot histogram of results
plt.hist(results, bins=50)
plt.title("Distribution of Annual Profits")
plt.xlabel("Profit ($)")
plt.ylabel("Frequency")
plt.show()