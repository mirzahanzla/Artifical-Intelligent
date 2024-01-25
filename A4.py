import numpy as np

def objective_function(x, y):
    return x**2 + y**2 + 10 * np.sin(x) + 10 * np.sin(y)

population_size = 50
generations = 100
mutation_rate = 0.01

x_lower_bound, x_upper_bound = -5, 5
y_lower_bound, y_upper_bound = -5, 5

# Create the initial population
def create_population():
    return np.random.uniform(low=[x_lower_bound, y_lower_bound], high=[x_upper_bound, y_upper_bound], size=(population_size, 2))

# Evaluate the fitness of each individual
def calculate_fitness(population):
    return objective_function(population[:, 0], population[:, 1])

def select_parents(population, fitness):
    tournament_size = 5
    tournament_indices = np.random.choice(len(population), tournament_size, replace=False)
    tournament_fitness = fitness[tournament_indices]
    return population[tournament_indices[np.argmin(tournament_fitness)]]

# Perform crossover to create a new generation
def crossover(parent1, parent2):
    crossover_point = np.random.rand()
    child = crossover_point * parent1 + (1 - crossover_point) * parent2
    return child

# Perform mutation on an individual
def mutate(individual):
    if np.random.rand() < mutation_rate:
        mutation_values = np.random.uniform(-0.5, 0.5, size=2)
        individual += mutation_values
    return individual

# Genetic Algorithm
def genetic_algorithm():
    population = create_population()
    for generation in range(generations):
        fitness = calculate_fitness(population)
        sorted_indices = np.argsort(fitness)
        population = population[sorted_indices]

        # Select parents and perform crossover to create new individuals
        new_population = []
        for _ in range(population_size // 2):
            parent1 = select_parents(population, fitness)
            parent2 = select_parents(population, fitness)
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            new_population.extend([child1, child2])

        population = np.array(new_population)

    # Return the best individual
    best_solution = population[0]
    best_fitness = objective_function(best_solution[0], best_solution[1])
    return best_solution, best_fitness

# Run the genetic algorithm and print the results
best_solution, best_fitness = genetic_algorithm()
print("Best Solution:", best_solution)
print("Best Fitness:", best_fitness)
