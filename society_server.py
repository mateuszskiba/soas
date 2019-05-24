from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter
from mesa.visualization.modules import ChartModule
from society import SocietyModel

chart = ChartModule([{"Label": "CooperationRatio",
                      "Color": "Red"}],
                    data_collector_name='dataCollector')
                    
n_slider = UserSettableParameter('number', "Number of Agents", 50, 2, 1000, 1)
neighbors = UserSettableParameter('number', "Number of neighbors", 10, 1, 100, 1)
min_neighbors = UserSettableParameter('number', "Minimal number of neighbors", 5, 1, 100, 1)
change_prob = UserSettableParameter('number', "Probability of random cooperation", 0.001, 0, 1)
change_prob_dev = UserSettableParameter('number', "Standard deviation of PRC", 0.001, 0, 1)
two_way = UserSettableParameter('checkbox', 'Two way switching', value=False)
server = ModularServer(SocietyModel,
                       [chart],
                       "Cooperation emergence moodel - homogenous group",
                       {"N": n_slider,
                        'changeProb': change_prob,
                        'changeProbDev': change_prob_dev,
                        'isCoop': False,
                        'neighbors': neighbors,
                        'minNeighbors': min_neighbors,
                        'twoWay': two_way
                        })
server.port = 8521  # The default
server.launch()