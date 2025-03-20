# Copyright 2022 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dimod import ConstrainedQuadraticModel, Binary, quicksum
from dwave.system import LeapHybridCQMSampler

values = [34, 25, 78, 21, 64]
weights = [3, 5, 9, 4, 2]
W = 10
n = len(values)

#TO-DO: Create the binary variables


#TO-DO: Construct the CQM


#TO-DO: Add the objective


#TO-DO: Add the weight constraints

cqm.add_constraint(quicksum(x[i] for i in range(n)) <= 2, label='max items')


#TO-DO: Define the Sampler

#TO-DO: Submit to the CQM sampler



sampleset = sampleset.aggregate()
print("\nFull sample set:")
print(sampleset)

feasible_sampleset = sampleset.filter(lambda row: row.is_feasible)
print("\nFeasible sample set:")
print(feasible_sampleset)

best_sample = feasible_sampleset.first.sample
value_string = "Values:\t\t"
value_sum = 0
weight_string = "Weights:\t"
weight_sum = 0
for i in range(n):
    if best_sample[i] < 1:
        value_string += '\tX'
        weight_string += '\tX'
    else:
        value_string += '\t'+str(values[i])
        value_sum += values[i]
        weight_string += '\t'+str(weights[i])
        weight_sum += weights[i]
value_string += '\tSum: '+str(value_sum)
weight_string += '\tSum: '+str(weight_sum)

print("\nBest solution found:")
print(value_string)
print(weight_string)