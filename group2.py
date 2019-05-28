from group import GroupModel
from mesa.datacollection import DataCollector


def compute_cooperation_ratio(model):
    cooperating = [int(agent.is_coop) for agent in model.schedule.agents]
    return sum(cooperating)/len(cooperating)


def compute_cooperation_ratio1(model):
    cooperating = [int(agent.is_coop) if agent.group_id == 0 else 0 for agent in model.schedule.agents]
    return sum(cooperating)/len(cooperating)


def compute_cooperation_ratio2(model):
    cooperating = [int(agent.is_coop) if agent.group_id == 1 else 0 for agent in model.schedule.agents]
    return sum(cooperating)/len(cooperating)


class GroupModel2(GroupModel):

    def __init__(self, n, n_ask_neigh, man1, man2, linear_coop, wtc1, wtc2, cp1, cp2, coop_prob_dev, debug=False):
        min_accept_neigh = [man1, man2]
        coop_prob = [cp1, cp2]
        wtc = [wtc1, wtc2]
        super().__init__(n, 2, n_ask_neigh, min_accept_neigh, linear_coop, wtc, coop_prob, coop_prob_dev, debug)

        self.data_collector = DataCollector(
            model_reporters={
                "CooperationRatio": compute_cooperation_ratio,
                "CooperationGroup1": compute_cooperation_ratio1,
                "CooperationGroup2": compute_cooperation_ratio2
            },
            agent_reporters={"IsCoop": "is_coop"}
        )

    def step(self):
        """Advance the model by one step."""
        self.data_collector.collect(self)
        self.schedule.step()
