import random

population_size = 10
generation_max = 20
gene_size = 12
mutate_chance = 0.2
parent_count = 5
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
def generate_population():
    population = []
    # generate 20 random genes
    for x in range(population_size):
        gene = []
        for g in range(gene_size):
            # generate random 1 or 0
            gene.append(random.randint(0,1))
        population.append(gene)

    return population

# mutate a random gene from 1 to 0 or 0 to 1
def mutate(target):
    index = random.randint(0, gene_size - 1)

    if target[index] == 0:
        target[index] = 1
    else:
        target[index] = 0

def evolve_population(population):
    # select parents by taking top ancestor_percentage (50%) and scraping the rest
    population = population[:5]
    # print selected parents
    print("Selected parents : ")
    for gene in population:
        print(tuple(gene))
    print("--------------------")
        
    # create 5 random children from 2 parents.
    print("Generated children : ")
    while len(population) < population_size:
        child = []
        parent1 = population[random.randint(0, parent_count - 1)]
        parent2 = population[random.randint(0, parent_count - 1)]

        child = parent1[:6] + parent2[6:]
        population.append(child)
        print(tuple(child))
    print("--------------------")

    # mutate with a probability
    for gene in population:
        if random.randint(0, 100) <= (100 * mutate_chance):
            mutate(gene)

    return population


# generate initial population (step 1)
population = generate_population()
for generation in range(generation_max):
    print("Generation %d" % (generation + 1))

    population = sorted(population, key=lambda x: fitness(x), reverse=True)

    for gene_index in range(population_size):
        print("%s , fitness: %.2f" % (tuple(population[gene_index]), fitness(population[gene_index])))

    # evolve here
    population = evolve_population(population)
    