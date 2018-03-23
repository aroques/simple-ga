from random import randint, choice

POPULATION_SIZE = 50
k = 2  # For binary tournament selection


def main():

    # Initialization
    population = get_population()
    print(population)

    # Selection
    parents = get_parents(population)
    print(parents)


def get_parents(population):
    parents = []
    for _ in range(2):
        parent = get_parent(population)
        parents.append(parent)
    return parents


def get_parent(population):
    """Use binary tournament selection to get a parent from the population"""
    samples = []
    for _ in range(k):
        sample = choice(population)
        samples.append(sample)
    fitnesses = [fitness_function(sample) for sample in samples]
    max_fitness = max(fitnesses)
    idx = fitnesses.index(max_fitness)
    return samples[idx]


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
