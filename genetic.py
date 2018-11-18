import random

yearly_budget = [3.1, 2.5, 0.4]

project_return = [0.2, 0.3, 0.5, 0.1]

cost = {
    1: [0.5, 1.0, 1.5, 0.1],
    2: [0.3, 0.8, 1.5, 0.4],
    3: [0.2, 0.2, 0.3, 0.1]
}

# the fitness is basically the highest achievable return
# as the cost does not matter as long as it does not go over budget
def fitness(target):
    year_one_cost = cost[1][0] * target[0] + cost[1][1] * target[1] + cost[1][2] * target[2] + cost[1][3] * target[3]
    year_two_cost = cost[2][0] * target[4] + cost[2][1] * target[5] + cost[2][2] * target[6] + cost[2][3] * target[7]
    year_three_cost = cost[3][0] * target[8] + cost[3][1] * target[9] + cost[3][2] * target[10] + cost[3][3] * target[11]

    if (year_one_cost > yearly_budget[0]) or (year_two_cost > yearly_budget[1]) or (year_three_cost > yearly_budget[2]):
        return 0

    # return the total money return
    return (target[0] + target[4] + target[8]) * project_return[0] + \
        (target[1] + target[5] + target[9]) * project_return[1] + \
        (target[2] + target[6] + target[10]) * project_return[2] + \
        (target[3] + target[7] + target[11]) * project_return[3]

    
