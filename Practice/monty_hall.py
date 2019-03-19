import random
import plotly.plotly as py
import plotly.graph_objs as go

py.sign_in(username='juupero', api_key='tTEKG7BDmroAIzImcY4e')


def one_try():
    """
    returns True if stick wins
    """
    behind_door_options = ['goat', 'goat', 'ferrari']
    random.shuffle(behind_door_options)
    print("Which door do you pick?")
    chosen_door = int(input("> "))
    if behind_door_options[chosen_door - 1] == 'ferrari':
        print("You won the Ferrari!!")
        return True
    else:
        print("No luck this time.")
        return False


def run_trials(trials):
    """
    run n trials and save number of both outcomes
    """
    won_count, lost_count = 0, 0
    while trials > 0:
        if one_try() == True:
            won_count += 1
        else:
            lost_count += 1
        trials -= 1
    print(str(won_count) + " " + str(lost_count))
    return (won_count, lost_count)



def display_sim(sim_result):
    """
    Make a piechart with plotly
    """

    labels = ['True', 'False']
    values = sim_result

    trace = go.Pie(labels=labels, values=values)

    py.iplot([trace], filename='basic_pie_chart')

display_sim(run_trials(5))