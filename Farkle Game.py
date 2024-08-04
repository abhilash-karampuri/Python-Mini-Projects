#farkle game
'''
Single 1s: Worth 100 points each.
Single 5s: Worth 50 points each.
Three of a kind: Worth 100 times the number on the die (e.g., three 2s = 200 points).
Four of a kind: Worth double the three of a kind score (e.g., four 2s = 400 points).
Five of a kind: Worth triple the three of a kind score (e.g., five 2s = 600 points).
Six of a kind: Worth quadruple the three of a kind score (e.g., six 2s = 800 points).
Straight (1-2-3-4-5-6): Worth 1500 points.
Three pairs: Worth 1500 points.
'''
from collections import Counter

def score_single_ones(dice):
    return dice.count(1) * 100

def score_single_fives(dice):
    return dice.count(5) * 50

def score_three_of_a_kind(dice):
    counts = Counter(dice)
    score = 0
    for value, count in counts.items():
        if count >= 3:
            score += 100 * value
    return score

def score_four_of_a_kind(dice):
    counts = Counter(dice)
    score = 0
    for value, count in counts.items():
        if count >= 4:
            score += 2 * (100 * value)
    return score

def score_five_of_a_kind(dice):
    counts = Counter(dice)
    score = 0
    for value, count in counts.items():
        if count >= 5:
            score += 3 * (100 * value)
    return score

def score_six_of_a_kind(dice):
    counts = Counter(dice)
    score = 0
    for value, count in counts.items():
        if count >= 6:
            score += 4 * (100 * value)
    return score

def score_straight(dice):
    if sorted(dice) == [1, 2, 3, 4, 5, 6]:
        return 1500
    return 0

def score_three_pairs(dice):
    counts = Counter(dice)
    if len(counts) == 3 and all(count == 2 for count in counts.values()):
        return 1500
    return 0

def calculate_score(dice):
    score = 0
    score += score_straight(dice)
    score += score_three_pairs(dice)
    score += score_six_of_a_kind(dice)
    score += score_five_of_a_kind(dice)
    score += score_four_of_a_kind(dice)
    score += score_three_of_a_kind(dice)
    score += score_single_ones(dice)
    score += score_single_fives(dice)
    return score

# Example usage
dice_roll = [1, 1, 1, 5, 5, 2]  # Replace with your dice roll
print(f"Score: {calculate_score(dice_roll)}")     