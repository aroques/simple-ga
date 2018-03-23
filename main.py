from random import randint, random, sample
from statistics import mean

POPULATION_SIZE = 50
CHANCE_OF_CROSSOVER = 0.6
NUM_MOST_FIT = 2


def main():
    # Initialization
    population = get_population()

    num_avg_same = num_generations = 0

    print_stats('-- Starting Population --', population)

    while num_avg_same < 3:
        num_generations += 1

        children = []
        num_pairs_of_children = (POPULATION_SIZE - NUM_MOST_FIT) / 2
        for _ in range(int(num_pairs_of_children)):
            # Selection
            parents = get_parents(population)

            # Recombination
            two_children = get_children(parents)
            children += two_children

        # Elitism Replacement - Keep the N=2 fittest individuals in population
        most_fit = get_most_fit_individuals(population)

        next_generation = children + most_fit

        num_avg_same += compare_populations(population, next_generation)

        population = next_generation

    print('Number of Generations: {}'.format(num_generations))
    print_stats('-- Final Generation --', next_generation)


def compare_populations(p1, p2):
    """Returns 1 if the two populations have the same fitness"""
    p1_fitnesses = get_fitnesses(p1)
    p2_fitnesses = get_fitnesses(p2)
    if mean(p1_fitnesses) == mean(p2_fitnesses):
        return 1
    else:
        return 0


def print_stats(title, population):
    fitnesses = get_fitnesses(population)
    print(title)
    print('Min: {}'.format(min(fitnesses)))
    print('Max: {}'.format(max(fitnesses)))
    print('Avg: {}'.format(mean(fitnesses)))


def get_most_fit_individuals(population):
    fitnesses = get_fitnesses(population)
    most_fit = []
    for i in range(NUM_MOST_FIT):
        the_fittest = max(fitnesses)
        fittest_idx = fitnesses.index(the_fittest)
        most_fit.append(population[fittest_idx])
    return most_fit


def get_children(parents):
    if random() <= CHANCE_OF_CROSSOVER:
        children = uniform_crossover(parents)
    else:
        children = parents
    return [mutate(child) for child in children]


def mutate(child):
    """Possibly flip each bit of child - on average one bit will be flipped"""
    length = len(child)
    child = list(child)
    chance_mutation = 1 / length
    for i in range(length):
        if random() > chance_mutation:
            continue
        if child[i] == '1':
            child[i] = '0'
        else:
            child[i] = '1'
    return ''.join(child)


def uniform_crossover(parents):
    """Uses uniform crossover to get two children from two parents"""
    string_len = len(parents[0])
    child = ''
    for i in range(string_len):
        parent_num = randint(0, 1)
        child += parents[parent_num][i]
    return child, invert_binary_string(child)


def invert_binary_string(binary_string):
    return ''.join('1' if bit == '0' else '0' for bit in binary_string)


def get_parents(population):
    parents = []
    for _ in range(2):
        parent = get_parent(population)
        parents.append(parent)
    return parents


def get_parent(population):
    """Use binary tournament selection to get a parent from the population"""
    s = sample(population, 2)
    fitnesses = get_fitnesses(s)
    max_fitness = max(fitnesses)
    fittest_idx = fitnesses.index(max_fitness)
    return s[fittest_idx]


def get_fitnesses(population):
    return [fitness_function(individual) for individual in population]


def fitness_function(binary_string):
    """OneMax - Returns number of ones in a string"""
    return binary_string.count('1')


def get_population():
    population = []
    string_size = get_positive_int_from_user()
    for _ in range(POPULATION_SIZE):
        binary_string = get_random_binary_string(string_size)
        population.append(binary_string)
    return population


def get_random_binary_string(string_size):
    binary_str = ''
    for _ in range(string_size):
        binary_str += str(randint(0, 1))
    return binary_str


def get_positive_int_from_user():
    n = -1
    while n < 1:
        try:
            n = int(input('Enter a positive integer:'))
        except ValueError as e:
            print('Please enter a positive integer')
    return n


if __name__ == '__main__':
    main()
