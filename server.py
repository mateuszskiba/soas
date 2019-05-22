from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter
from mesa.visualization.modules import ChartModule
from society import SocietyModel

chart = ChartModule([{"Label": "CooperationRatio",
                      "Color": "Red"}],
                    data_collector_name='dataCollector')
n_slider = UserSettableParameter('slider', "Number of Agents", 2, 2, 100, 1)
neighbors = UserSettableParameter('slider', "Number of neighbors", 1, 1, 100, 1)
min_neighbors = UserSettableParameter('slider', "Minimal number of neighbors", 1, 1, 100, 1)
change_prob = UserSettableParameter('number', "Probability of random cooperation", 0, 0,1)

server = ModularServer(SocietyModel,
                       [chart],
                       "Society model",
                       {"N": n_slider,
                        'changeProb': change_prob,
                        'isCoop': False,
                        'neighbors': neighbors,
                        'minNeighbors': min_neighbors
                        })
server.port = 8521 # The default
server.launch()