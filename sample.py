# sample implementation of AHP
import numpy as np
from ahp import Hierarchy, Layer


# initialize a hierarchy
ahp = Hierarchy()

# initialize layers
criteria_labels = ['availability', 'difficulty', 'preference']
alternative_labels = ['AMAT 115', 'AMAT 160', ' AMAT 162', 'AMAT 163']
criteria = Layer(num_input=1, num_output=3, labels=criteria_labels, unique_id='criteria')
alternatives = Layer(num_input=3, num_output=4, labels=alternative_labels, unique_id='alternatives')

# build hierarchy model
ahp.add(criteria)
ahp.add(alternatives)

# show currrent weights and labels of hierarchy model
ahp.report()

# variables for updating weights
A = np.array(
    [[1, 3, 5],
     [1/3, 1, 2],
     [1/5, 1/2, 1]]
     )
availability = [30, 25, 35, 25]
difficulty = np.array([
    [1,4,3,2],
    [1/4,1,1/2,1/3],
    [1/3,2,1,1/2],
    [1/2,3,2,1]
])
preference = [1, 4, 3, 2]

# updating weights
print()
print('Updating criteria and alternatives weights ...')
criteria.update_weights(input_type='matrix', comparison_matrix=A)
alternatives.update_weights(layer_idx=0, input_type='values', values=availability)
alternatives.update_weights(layer_idx=1, input_type='matrix', comparison_matrix=difficulty)
alternatives.update_weights(layer_idx=2, input_type='rank', ranking=preference)

# show updated weights
print()
ahp.report()

# solve for decision weights
print()
decision_weights = ahp.compute_decision()
