import random

equation = lambda a, b: 2*a + b
target = 45
error = 3

size = 70
mutation_rate = 0.1
total_generations = 1000

def calculate_fitness(a, b):
    return abs(equation(a, b) - target)

def starting_population(size):
    return [(random.uniform(0, 10), random.uniform(0, 10)) for _ in range(size)]

def mutation(individual):
    return (individual[0] + random.uniform(-mutation_rate, mutation_rate),
            individual[1] + random.uniform(-mutation_rate, mutation_rate))

def crossover(parent1, parent2):
    return ((parent1[0] + parent2[0]) / 2, (parent1[1] + parent2[1]) / 2)

def genetic_algorithm():
    population = starting_population(size)

    for generation in range(total_generations):
        population = sorted(population, key=lambda x: calculate_fitness(x[0], x[1]))

        if calculate_fitness(population[0][0], population[0][1]) <= error:
            print("Solution found in generation", generation)
            print("a =", population[0][0])
            print("b =", population[0][1])
            return

        new_population = [population[0]]  
        for i in range(1, size):
            parent1 = random.choice(population[:10])  
            parent2 = random.choice(population[:10])
            child = crossover(parent1, parent2)
            child = mutation(child)
            new_population.append(child)

        population = new_population

    print("No solution found within the specified total_generations.")

genetic_algorithm()
