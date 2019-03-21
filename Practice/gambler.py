import random


def one_try(coins, goal):
  """
  place bets while there is at least 1 coin left
  probability of winning is 50%, increment/decrement
  coins after each run, return tuple
  (number_of_bets: int, won: boolean)
  """
  number_of_bets, won, coin_flip_results = 0, False, [-1, 1]

  while coins > 1:
    random.shuffle(coin_flip_results)
    coins += coin_flip_results[0]
    number_of_bets += 1
    if coins == goal:
      won = True
      break
  return(number_of_bets, won)

def run_n_trials(coins, goal, trials):
  """
  Run simulation with n trials
  return list of tuples (number_of_bets: int, won: boolean)
  """
  result_list = []
  while trials > 0:
    result_list.append(one_try(coins, goal))
    trials -= 1
  return result_list

def get_average_winrate(results):
    """
    Calculate average win rate based on the data returned
    from run_n_trials
    """
    trials, wins = 0, 0
    for a, b in results:
      trials += 1
      if b is True:
        wins += 1
    win_rate = wins / trials * 100
    print(f"The average win rate was: {win_rate} %" )


get_average_winrate(run_n_trials(70, 100, 10000))