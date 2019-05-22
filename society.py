from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
from mesa.batchrunner import BatchRunner
import numpy as np


def computeCooperationRatio(model):
    cooperating = [int(agent.isCoop) for agent in model.schedule.agents]
    return sum(cooperating)/len(cooperating)


class SocietyModel(Model):
    """A model with some number of social agents."""

    def __init__(self, N, changeProb, isCoop, neighbors, minNeighbors, debug=False):
        self.agentConfig = {
                'changeProb': changeProb,
                'isCoop': isCoop,
                'pNeighbors': neighbors,
                'minCoop': minNeighbors
            }
        self.numAgents = N
        self.schedule = RandomActivation(self)
        self.debug = debug
        self.running = True
        # Activates all the agents once per step in random order, should be considered a parameter

        # Create agents
        for i in range(self.numAgents):
            socialAgent = SocialAgent(i, self.agentConfig, self)
            self.schedule.add(socialAgent)

        self.dataCollector = DataCollector(
            model_reporters={"CooperationRatio": computeCooperationRatio},
            agent_reporters={"IsCoop": "isCoop"}
        )

    def askNeighbors(self, howMany):
        cooperating = np.array([int(agent.isCoop) for agent in self.schedule.agents])
        np.random.shuffle(cooperating)
        return sum(cooperating[:howMany])

    def totalCooperation(self):
        return sum([int(agent.isCoop) for agent in self.schedule.agents]) == self.numAgents


    def step(self):
        '''Advance the model by one step.'''
        self.dataCollector.collect(self)  # collect data
        self.schedule.step()
        if self.totalCooperation():
            self.running = False


class SocialAgent(Agent):
    """ A social agent."""

    def __init__(self, unique_id, agentConfig, model):
        super().__init__(unique_id, model)
        self.changeProb = agentConfig['changeProb']
        self.isCoop = agentConfig['isCoop']
        self.nNeighbors = agentConfig['pNeighbors']
        self.minCop = agentConfig['minCoop']

    def requirementsMet(self):
        if not(self.model.askNeighbors(self.nNeighbors) >= self.minCop): # if the min number of cooperating agents isn't reached
            return False
        return True

    def shouldCooperate(self):
        # Function asnwering the question if the agent is cooperating
        if self.requirementsMet() and not(self.isCoop):
            self.isCoop = True
            return self.isCoop

        elif not(self.isCoop):
            self.isCoop = np.random.rand() >= 1 - self.changeProb
            return self.isCoop
        
        else:
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
