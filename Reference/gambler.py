import random


def one_try(coins, goal):
    bets = 0
    while 0 < coins < goal:
        coins += (1 if random.randint(0,1) else -1)
        bets += 1
    return bets, coins == goal


def run_n_trials(coins, goal, trials):
    results = []
    for _ in range(trials):
        results.append(one_try(coins, goal))
    return results


def get_average_winrate(results):
    total = len(results)
    wins = len([game for game in results if game[1]])
    avg_winrate = round(wins / float(total) * 100.0)
    return avg_winrate


coins = 3
goal = 10
trials = 100

results = run_n_trials(coins, goal, trials)
# print(results)
print(f'{get_average_winrate(results)} %')
