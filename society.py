from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
import numpy as np

def computeCooperationRatio(model):
    cooperating = [int(agent.isCoop) for agent in model.schedule.agents]
    return sum(cooperating)/len(cooperating)

class SocietyModel(Model):
    """A model with some number of social agents."""

    def __init__(self, N, agentConfig, debug=False):
        self.numAgents = N
        self.schedule = RandomActivation(self)
        self.debug = debug
        # Activates all the agents once per step in random order, should be considered a parameter

        # Create agents
        for i in range(self.numAgents):
            socialAgent = SocialAgent(i, agentConfig, self)
            self.schedule.add(socialAgent)

        self.dataCollector = DataCollector(
            model_reporters={"CooperationRatio": computeCooperationRatio},
            agent_reporters={"IsCoop": "isCoop"}
        )

    def step(self):
        '''Advance the model by one step.'''
        self.dataCollector.collect(self) # collect data
        self.schedule.step()



class SocialAgent(Agent):
    """ A social agent."""

    def __init__(self, unique_id, agentConfig, model):
        super().__init__(unique_id, model)
        self.changeProb = agentConfig['changeProb']
        self.isCoop = agentConfig['isCoop']

    def shouldCooperate(self):
        # Function asnwering the question if the agent is cooperating
        if self.isCoop:
            return True
        else:
            self.isCoop = np.random.rand() >= 1 - self.changeProb
            return self.isCoop

    def printStatus(self):
        if not(self.model.debug):
            return
        status = "ID: %d\t Cooperating: %d" % (self.unique_id, self.isCoop)
        print(status)

    def step(self):
        # If the agent is a defector every step it decides wether to cooperate
        self.shouldCooperate()
        self.printStatus()
