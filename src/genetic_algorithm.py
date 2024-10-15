import random

class GeneticAlgorithm:
    """
    Implementa um algoritmo genético para resolver o problema da mochila.
    """

    def __init__(self, problem, population_size, crossover_rate, mutation_rate, num_generations, selection_method='tournament', tournament_size=5, elitism=False):
        """
        Inicializa uma nova instância do algoritmo genético.
        """
        self.problem = problem
        self.population_size = population_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.num_generations = num_generations
        self.selection_method = selection_method
        self.tournament_size = tournament_size
        self.elitism = elitism

    def run(self):
        """
        Executa o algoritmo genético.
        """
        population = self.generate_initial_population()
        best_solution = None
        best_fitness = 0

        for generation in range(self.num_generations):
            print(f"\nGeração {generation + 1}")
            fitness_scores = [self.problem.evaluate_fitness(individual) for individual in population]
            
            if self.elitism:
                elite = max(zip(population, fitness_scores), key=lambda x: x[1])[0]

            new_population = []
            while len(new_population) < self.population_size:
                parent1 = self.selection(population, fitness_scores)
                parent2 = self.selection(population, fitness_scores)
                child = self.crossover(parent1, parent2)
                self.mutate(child)
                new_population.append(child)

            if self.elitism:
                new_population[0] = elite

            population = new_population

            current_best = max(zip(population, fitness_scores), key=lambda x: x[1])
            if current_best[1] > best_fitness:
                best_solution, best_fitness = current_best

            print(f"Melhor fitness na geração {generation + 1}: {best_fitness}")

        return best_solution, best_fitness

    def generate_initial_population(self):
        """
        Gera a população inicial aleatoriamente.
        """
        return [[random.choice([0, 1]) for _ in range(len(self.problem.items))] for _ in range(self.population_size)]

    def selection(self, population, fitness_scores):
        """
        Seleciona um indivíduo da população usando o método de seleção especificado.
        """
        if self.selection_method == 'tournament':
            return self.tournament_selection(population, fitness_scores)
        elif self.selection_method == 'roulette':
            return self.roulette_selection(population, fitness_scores)
        else:
            raise ValueError("Invalid selection method")

    def tournament_selection(self, population, fitness_scores):
        """
        Realiza a seleção por torneio.
        """
        tournament = random.sample(list(zip(population, fitness_scores)), self.tournament_size)
        return max(tournament, key=lambda x: x[1])[0]

    def roulette_selection(self, population, fitness_scores):
        """
        Realiza a seleção por roleta.
        """
        total_fitness = sum(fitness_scores)
        pick = random.uniform(0, total_fitness)
        current = 0
        for individual, fitness in zip(population, fitness_scores):
            current += fitness
            if current > pick:
                return individual

    def crossover(self, parent1, parent2):
        """
        Realiza o cruzamento entre dois pais para gerar um filho.
        """
        if random.random() < self.crossover_rate:
            crossover_point = random.randint(1, len(parent1) - 1)
            child = parent1[:crossover_point] + parent2[crossover_point:]
            
            print("\nCruzamento realizado:")
            print(f"Pai 1: {parent1}")
            print(f"Pai 2: {parent2}")
            print(f"Ponto de cruzamento: {crossover_point}")
            print(f"Filho: {child}")
            
            return child
        else:
            print("\nCruzamento não realizado. Retornando cópia do Pai 1.")
            return parent1.copy()

    def mutate(self, individual):
        """
        Aplica mutação a um indivíduo.
        """
        for i in range(len(individual)):
            if random.random() < self.mutation_rate:
                individual[i] = 1 - individual[i]  # Flip the bit