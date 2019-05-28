from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter
from mesa.visualization.modules import ChartModule
from group2 import GroupModel2
import numpy as np

chart_all = ChartModule([{"Label": "CooperationRatio",
                          "Color": "Red"}],
                        data_collector_name='data_collector')

chart_1 = ChartModule([{"Label": "CooperationGroup1",
                        "Color": "Blue"}],
                      data_collector_name='data_collector')

chart_2 = ChartModule([{"Label": "CooperationGroup2",
                        "Color": "Green"}],
                      data_collector_name='data_collector')

n_groups = 2
np.random.seed(1)

n = UserSettableParameter('number', "Number of Agents", 30, 3, 1000, 1)
n_ask_neigh = UserSettableParameter('number', "Number of neighbors to ask", 10, 1, 100, 1)
cp1 = UserSettableParameter('number', "Probability of random cooperation (group 1)", 0.01, 0, 1)
cp2 = UserSettableParameter('number', "Probability of random cooperation (group 2)", 0.015, 0, 1)
# willing to cooperate: > 1 more willing to cooperate
#                       < 1 less willing to cooperate
#                       = 1 normal
wtc1 = UserSettableParameter('number', "Willing to cooperate (group 1)", 1.4, 0, 1)
wtc2 = UserSettableParameter('number', "Willing to cooperate (group 2)", 1.0, 0, 1)
coop_prob_dev = UserSettableParameter('slider', "Standard deviation of PRC", 0.000, 0, 1, step=0.001)

server = ModularServer(GroupModel2,
                       [chart_all,
                        chart_1,
                        chart_2],
                       "Group model",
                       {"n": n,
                        'n_ask_neigh': n_ask_neigh,
                        'man1': None,
                        'man2': None,
                        'linear_coop': True,
                        'wtc1': wtc1,
                        'wtc2': wtc2,
                        'cp1': cp1,
                        'cp2': cp2,
                        'coop_prob_dev': coop_prob_dev
                        })
server.port = 8521  # The default
server.launch()
