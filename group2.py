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

    def __init__(self, n, n_ask_neigh, man1, man2, cp1, cp2, coop_prob_dev, debug=False):
        min_accept_neigh = [man1, man2]
        coop_prob = [cp1, cp2]
        super().__init__(n, 2, n_ask_neigh, min_accept_neigh, coop_prob, coop_prob_dev, debug)

        self.dataCollector = DataCollector(
            model_reporters={
                "CooperationRatio": compute_cooperation_ratio,
                "CooperationGroup1": compute_cooperation_ratio1,
                "CooperationGroup2": compute_cooperation_ratio2
            },
            agent_reporters={"IsCoop": "is_coop"}
        )
