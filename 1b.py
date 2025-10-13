players = [
    {"name": "Kohli", "strengths": {"chase_master", "fast_bowling_destroyer", "fielding"}, "weaknesses": {"left_arm_spin"}},
    {"name": "Rahul", "strengths": {"opener", "power_play", "wicketkeeping"}, "weaknesses": {"pressure", "death_bowling"}},
    {"name": "Bumrah", "strengths": {"death_bowling", "yorkers", "economy"}, "weaknesses": {"batting"}},
    {"name": "Jadeja", "strengths": {"power_hitting", "off_spin", "fielding"}, "weaknesses": set()},
    {"name": "Maxwell", "strengths": {"spin_bowling", "fielding", "finisher"}, "weaknesses": {"pace_bounce", "consistency"}},
    {"name": "Siraj", "strengths": {"swing_bowling", "new_ball"}, "weaknesses": {"batting"}},
    {"name": "Shreyas", "strengths": {"middle_order", "spin_hitter"}, "weaknesses": {"express_pace", "short_ball"}},
    {"name": "Chahal", "strengths": {"leg_spin", "wicket_taker"}, "weaknesses": {"fielding", "batting", "expensive"}},
    {"name": "DK", "strengths": {"finisher", "wicketkeeping", "experience"}, "weaknesses": {"poor_wicketkeeping"}},
    {"name": "Faf", "strengths": {"opener", "experience", "fielding"}, "weaknesses": {"slow_starter"}}
]
def weakness_penalty(weaknesses):
    penalty = 0
    if "batting" in weaknesses and "poor_wicketkeeping" in weaknesses:
        penalty -= 1
    if "consistency" in weaknesses and "pressure" in weaknesses:
        penalty -= 1
    if "slow_starter" in weaknesses and "pressure" in weaknesses:
        penalty -= 1
    return penalty

def role_bonus(team):
    has_opener = any("opener" in p["strengths"] for p in team)
    has_bowler = any("death_bowling" in p["strengths"] or "swing_bowling" in p["strengths"] or "spin_bowling" in p["strengths"] or "leg_spin" in p["strengths"] for p in team)
    has_finisher = any("finisher" in p["strengths"] for p in team)
    has_wicketkeeper = any("wicketkeeping" in p["strengths"] for p in team)
    bonus = 0
    if has_opener: bonus += 1
    if has_bowler: bonus += 1
    if has_finisher: bonus += 1
    if has_wicketkeeper: bonus += 1
    return bonus



def team_score(team):
    strengths = set()
    weaknesses = set()

    for player in team:
        strengths |= player["strengths"]
        weaknesses |= player["weaknesses"]
        
    score = len(strengths) - len(weaknesses)

    score += role_bonus(team)
    score += weakness_penalty(weaknesses)

    return score, strengths, weaknesses


from itertools import combinations

def best_team(players, k):
    best_score = -10000
    best_combination = None
    for combo in combinations(players, k):
        score, strengths, weaknesses = team_score(combo)
        if score > best_score:
            best_score = score
            best_combination = (combo, strengths, weaknesses)
    return best_combination, best_score

team, score = best_team(players, 3)
print("Best Team:")
print([p["name"] for p in team[0]])
print(f"Net Score: {score}")
print(f"Unique Strengths: {len(team[1])}, Weaknesses: {len(team[2])}")

