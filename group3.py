from group import GroupModel


class GroupModel3(GroupModel):

    def __init__(self, n, n_ask_neigh, man1, man2, man3, cp1, cp2, cp3, coop_prob_dev, debug=False):
        min_accept_neigh = [man1, man2, man3]
        coop_prob = [cp1, cp2, cp3]
        super().__init__(n, 3, n_ask_neigh, min_accept_neigh, coop_prob, coop_prob_dev, debug)
