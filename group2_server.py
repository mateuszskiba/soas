from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter
from mesa.visualization.modules import ChartModule
from group2 import GroupModel2

chart_all = ChartModule([{"Label": "CooperationRatio",
                          "Color": "Red"}],
                        data_collector_name='dataCollector')

chart_1 = ChartModule([{"Label": "CooperationGroup1",
                        "Color": "Blue"}],
                      data_collector_name='dataCollector')

chart_2 = ChartModule([{"Label": "CooperationGroup2",
                        "Color": "Green"}],
                      data_collector_name='dataCollector')

n_groups = 2

n = UserSettableParameter('number', "Number of Agents", 30, 3, 1000, 1)
n_ask_neigh = UserSettableParameter('number', "Number of neighbors to ask", 10, 1, 100, 1)
man1 = UserSettableParameter('number', "Minimal accepts required from asked neighbors (group 1)", 9, 1, 100, 1)
man2 = UserSettableParameter('number', "Minimal accepts required from asked neighbors (group 2)", 4, 1, 100, 1)
cp1 = UserSettableParameter('number', "Probability of random cooperation (group 1)", 0.2, 0, 1)
cp2 = UserSettableParameter('number', "Probability of random cooperation (group 2)", 0.1, 0, 1)
coop_prob_dev = UserSettableParameter('slider', "Standard deviation of PRC", 0.000, 0, 1, step=0.001)

server = ModularServer(GroupModel2,
                       [chart_all,
                        chart_1,
                        chart_2],
                       "Group model",
                       {"n": n,
                        'n_ask_neigh': n_ask_neigh,
                        'man1': man1,
                        'man2': man2,
                        'cp1': cp1,
                        'cp2': cp2,
                        'coop_prob_dev': coop_prob_dev
                        })
server.port = 8521  # The default
server.launch()
