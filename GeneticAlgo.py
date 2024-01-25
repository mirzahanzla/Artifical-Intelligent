import random


def fitness_function(instances_list):
    global goal, gen
    gen += 1

    def fitness(item):
        cal_output = 2 * pow(item, 2) + 45
        if cal_output == goal - 2 or cal_output == goal + 2 or cal_output == goal:
            print(f'The individual with value : {cal_output} is nearest to goal after generation {gen}')
            exit()
        return abs(goal - cal_output)

    sorted_list = sorted(instances_list, key=fitness)
    binary_code(sorted_list)


def binary_code(sorted_list):
    binary_code_list = []
    for element in sorted_list:
        binary_code_list.append(bin(element)[2:])

    cross_over(binary_code_list)


def cross_over(binary_list):
    offspring = []
    for i, (ele) in enumerate(binary_list):
        if i >= len(binary_list) - 1:
            break
        parent_1 = binary_list[i]
        parent_2 = binary_list[i + 1]

        if len(parent_1) != len(parent_2):
            diff = len(parent_1) - len(parent_2)
            append_zeros = '0' * abs(diff)
            if diff > 0:
                parent_2 = append_zeros + parent_2
            else:
                parent_1 = append_zeros + parent_1

        crossover_point = random.randint(0, len(parent_1) - 1)
        child_1 = replace_bits(parent_1, parent_2, crossover_point, crossover_point + 2)
        child_2 = replace_bits(parent_2, parent_1, crossover_point, crossover_point + 2)
        offspring.append(child_1)
        offspring.append(child_2)

    mutation(offspring)


def replace_bits(parent_1, parent_2, swap_point1, swap_point2):
    return parent_1[:swap_point1] + parent_2[swap_point1:swap_point2] + parent_1[swap_point2:]


def mutation(offspring):
    for i, element in enumerate(offspring):
        flip_point = random.randint(0, len(element) - 1)
        bit_list = list(element)
        if bit_list[flip_point] == '0':
            bit_list[flip_point] = '1'
        else:
            bit_list[flip_point] = '0'

        offspring[i] = ''.join(bit_list)

    decimal_list = [int(binary, 2) for binary in offspring]
    fitness_function(decimal_list)


goal = 245
my_list = [24, 12, 233, 450, 231, 11]
gen = 0
fitness_function(my_list)
