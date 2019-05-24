from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter
from mesa.visualization.modules import ChartModule
from group3 import GroupModel3

chart = ChartModule([{"Label": "CooperationRatio",
                      "Color": "Red"}],
                    data_collector_name='dataCollector')
n_groups = 3

n = UserSettableParameter('number', "Number of Agents", 30, 3, 1000, 1)
n_ask_neigh = UserSettableParameter('number', "Number of neighbors to ask", 10, 1, 100, 1)
man1 = UserSettableParameter('number', "Minimal accepts required from asked neighbors (group 1)", 15, 1, 100, 1)
man2 = UserSettableParameter('number', "Minimal accepts required from asked neighbors (group 2)", 10, 1, 100, 1)
man3 = UserSettableParameter('number', "Minimal accepts required from asked neighbors (group 3)", 5, 1, 100, 1)
cp1 = UserSettableParameter('number', "Probability of random cooperation (group 1)", 0.25, 0, 1)
cp2 = UserSettableParameter('number', "Probability of random cooperation (group 2)", 0.15, 0, 1)
cp3 = UserSettableParameter('number', "Probability of random cooperation (group 3)", 0.05, 0, 1)
coop_prob_dev = UserSettableParameter('slider', "Standard deviation of PRC", 0.000, 0, 1, step=0.001)

server = ModularServer(GroupModel3,
                       [chart],
                       "Group model",
                       {"n": n,
                        'n_ask_neigh': n_ask_neigh,
                        'man1': man1,
                        'man2': man2,
                        'man3': man3,
                        'cp1': cp1,
                        'cp2': cp2,
                        'cp3': cp3,
                        'coop_prob_dev': coop_prob_dev
                        })
server.port = 8521  # The default
server.launch()
