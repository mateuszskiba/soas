from society import SocietyModel
from matplotlib import pyplot as plt

agentConfig = {
    'changeProb' : 0.01,
    'isCoop' : False
}

model = SocietyModel(100, agentConfig, debug=False)

for i in range(10):
    model.step()

plt.plot(model.dataCollector.get_model_vars_dataframe())
plt.show()