from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
from mesa.batchrunner import BatchRunner
import numpy as np


def compute_cooperation_ratio(model):
    cooperating = [int(agent.is_coop) for agent in model.schedule.agents]
    return sum(cooperating)/len(cooperating)


class GroupModel(Model):
    """A model with some number of agents."""
    def __init__(self, n, n_groups, n_ask_neigh, min_accept_neigh, coop_prob, coop_prob_dev, debug=False):
        super().__init__()
        self.num_agents = n
        self.schedule = RandomActivation(self)
        self.debug = debug

        assert n_groups == len(coop_prob)
        assert n % n_groups == 0
        div = n / n_groups

        for i in range(self.num_agents):
            group_id = int(i // div)
            agent_config = {
                'group_id': group_id,
                'n_ask_neigh': n_ask_neigh,
                "min_accept_neigh": min_accept_neigh[group_id],
                'coop_prob': coop_prob[group_id],
                'coop_prob_dev': coop_prob_dev
            }
            a = GroupAgent(i, agent_config, self)
            self.schedule.add(a)

        # self.dataCollector = DataCollector(
        #     model_reporters={"CooperationRatio": compute_cooperation_ratio},
        #     agent_reporters={"IsCoop": "is_coop"}
        # )

    def step(self):
        """Advance the model by one step."""
        self.dataCollector.collect(self)
        self.schedule.step()

    def ask_neighbors(self, n_ask_neigh):
        responses = np.array([int(agent.is_coop) for agent in self.schedule.agents])
        np.random.shuffle(responses)
        return np.sum(responses[:n_ask_neigh])

    # def ask_my_group(self, group_id):
    #     groupmates = []
    #     for a in self.schedule.agents:
    #         if a.group_id == group_id:
    #             groupmates.append(a)
    #     coop_list = np.array([int(a.is_coop) for a in groupmates])
    #     return np.sum(coop_list) > (coop_list.shape[0] / 2.0)
    #     # groupmates = np.array([int(agent.isCoop) for agent in self.schedule.agents])


class GroupAgent(Agent):

    def __init__(self, unique_id, agent_config, model):
        super().__init__(unique_id, model)
        self.group_id = agent_config['group_id']
        self.n_ask_neigh = agent_config['n_ask_neigh']
        self.min_accept_neigh = agent_config['min_accept_neigh']
        self.coop_prob = agent_config['coop_prob']
        self.is_coop = False
        # self.sum = 0

    def decide(self):
        if np.random.rand() >= 1 - self.coop_prob:
            self.is_coop = True
        else:
            self.is_coop = self.model.ask_neighbors(self.n_ask_neigh) >= self.min_accept_neigh
        return self.is_coop

    def step(self):
        self.decide()
        # self.sum += np.random.randint(self.group_id+2)
