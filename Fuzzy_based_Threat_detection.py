import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Define input variables
physical_threat = ctrl.Antecedent(np.arange(0, 11, 1), 'physical_threat')
cyber_threat = ctrl.Antecedent(np.arange(0, 11, 1), 'cyber_threat')

# Define output variable
threat_level = ctrl.Consequent(np.arange(0, 11, 1), 'threat_level')

# Automatically generate fuzzy sets for input variables
physical_threat.automf(3)
cyber_threat.automf(3)

# Automatically generate fuzzy sets for output variable
threat_level.automf(3)

# Define rules
rules = [
    ctrl.Rule(physical_threat['poor'] | cyber_threat['poor'], threat_level['poor']),
    ctrl.Rule(physical_threat['average'] & cyber_threat['average'], threat_level['average']),
    ctrl.Rule(physical_threat['good'] | cyber_threat['good'], threat_level['good'])
]

# Create and simulate the fuzzy system
threat_eval = ctrl.ControlSystem(rules)
threat_evaluator = ctrl.ControlSystemSimulation(threat_eval)

# Pass inputs and evaluate the system
threat_evaluator.input['physical_threat'] = 3.5  # Example physical threat level
threat_evaluator.input['cyber_threat'] = 7.2  # Example cyber threat level
threat_evaluator.compute()

# Output result
print("Threat level:", threat_evaluator.output['threat_level'])
threat_level.view(sim=threat_evaluator)

plt.show()