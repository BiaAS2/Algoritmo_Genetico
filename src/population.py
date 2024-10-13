import random
from .candidate import Candidate


class Population:
    def __init__(self, size, num_genes):
        self.individuals = [Candidate(self.random_genome(num_genes)) for _ in range(size)]

    def random_genome(self, num_genes):
        return [random.randint(0, 1) for _ in range(num_genes)]

    def evolve(self, items, capacity, crossover_rate, mutation_rate):
        next_generation = []
        for _ in range(len(self.individuals)):
            parent1 = self.tournament_selection(items, capacity)
            parent2 = self.roulette_selection(items, capacity)
            offspring = self.crossover(parent1, parent2, crossover_rate)
            self.mutate(offspring, mutation_rate)
            next_generation.append(offspring)
        self.individuals = next_generation

    def tournament_selection(self, items, capacity, tournament_size=5):
        tournament = random.sample(self.individuals, tournament_size)
        best = max(tournament, key=lambda ind: ind.calculate_fitness(items, capacity))
        return best

    def roulette_selection(self, items, capacity):
        total_fitness = sum(ind.calculate_fitness(items, capacity) for ind in self.individuals)
        random_fitness = random.uniform(0, total_fitness)
        cumulative_fitness = 0
        for ind in self.individuals:
            cumulative_fitness += ind.calculate_fitness(items, capacity)
            if cumulative_fitness >= random_fitness:
                return ind

    # Cruzamento de dois pontos
    def crossover(self, parent1, parent2, crossover_rate):
        if random.random() < crossover_rate:
            crossover_point = random.randint(1, len(parent1.genome) - 1)
            crossover_point2 = random.randint(crossover_point, len(parent1.genome) - 1)
            child_genome = (parent1.genome[:crossover_point] +
                            parent2.genome[crossover_point:crossover_point2] + parent1.genome[crossover_point2:])
            return Candidate(child_genome)
        return parent1

    def mutate(self, individual, mutation_rate):
        for i in range(len(individual.genome)):
            if random.random() < mutation_rate:
                individual.genome[i] = 1 - individual.genome[i]
