"""
    "Underwriting Profits: The Hidden Dynamics of Insurance Success"
"""

import numpy as np


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
