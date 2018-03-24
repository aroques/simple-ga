# Simple Genetic Algorithm

A simple genetic algorithm that solves the one-max problem.

The population size starts at size 10. Then, the GA is ran 5 times. Next, we check to see if the global optimum is present in each of the 5 new generations. If it is not, then we then double the population size and repeat the above procedure. Once we find the smallest population size where the global optimum is in each of the 5 generations we have found and upper bound. Next, we take the midpoint betweem this upperbound and the a lower bound where it last failed. We repeat this procedure until we find a minimum population size. This procedure of finding the minimum population size to solve a problem is called bisection.

Binary tournament selection is used to select parents. Then, there is a 60% chance that uniform crossover will be applied to those parents to produce two new children for the 'next generation'. Otherwise, there is a 40% chance that the parents will be kept in the 'new generation'.
