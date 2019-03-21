import random
import plotly.plotly as py
import plotly.graph_objs as go


py.sign_in(username='isaevpd', api_key='')


def one_try():
    """
    returns True if stick wins
    """
    doors = ['goat', 'goat', 'car']
    random.shuffle(doors)
    choice = doors.pop(0)
    doors.remove('goat')
    # True if stick wins
    return choice == 'car'


def run_trials(trials):
    stick_wins = 0
    swap_wins = 0
    for _ in range(trials):
        if one_try():
            stick_wins += 1
        else:
            swap_wins += 1

    return (stick_wins, swap_wins)


def display_sim(sim_result, title):
    labels = ['Stick', 'Swap']

    trace = go.Pie(labels=labels, values=sim_result)
    py.iplot([trace], filename=title)


sim_result = run_trials(10000)
display_sim(sim_result, 'Monty hall')   
