from random import randint, choice, random

POPULATION_SIZE = 50
CHANCE_OF_CROSSOVER = 0.6
k = 2  # For binary tournament selection


def main():

    # Initialization
    population = get_population()
    print(population)

    # Selection
    parents = get_parents(population)
    print(parents)

    # Recombination
    children = get_children(parents)

    print(children)


def get_children(parents):
    if random() <= CHANCE_OF_CROSSOVER:
        children = uniform_crossover(parents)
    else:
        children = parents
    return [mutate(child) for child in children]


def mutate(child):
    length = len(child)
    child = list(child)
    CHANCE_MUTATION = 1 / length
    for i in range(length):
        if random() > CHANCE_MUTATION:
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
    samples = get_samples(population, k)
    fitnesses = [fitness_function(sample) for sample in samples]
    max_fitness = max(fitnesses)
    idx = fitnesses.index(max_fitness)
    return samples[idx]


def get_samples(population, k):
    """Returns list of k samples from population"""
    samples = []
    for _ in range(k):
        sample = choice(population)
        samples.append(sample)
    return samples


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
