import random
class GeneticAlgorithm:
    """
    Implementa um algoritmo genético para problemas de otimização.

    Esta classe fornece métodos para executar um algoritmo genético, incluindo
    inicialização da população, seleção, cruzamento e mutação.
    """
    def __init__(self, problem, population_size, crossover_rate, mutation_rate, num_generations, selection_method='tournament', tournament_size=5, elitism=False):
        """
        Inicializa o GeneticAlgorithm com os parâmetros do problema.

        Args:
            problem: O problema a ser resolvido, deve ter um método evaluate_fitness.
            population_size (int): O número de indivíduos em cada geração.
            crossover_rate (float): A probabilidade de ocorrer cruzamento.
            mutation_rate (float): A probabilidade de um gene sofrer mutação.
            num_generations (int): O número de gerações para executar o algoritmo.
            selection_method (str): O método usado para seleção ('tournament' ou 'roulette').
            tournament_size (int): O número de indivíduos em cada seleção por torneio.
            elitism (bool): Se deve usar elitismo (preservar o melhor indivíduo).
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

        Returns:
            tuple: Uma tupla contendo a melhor solução encontrada, sua aptidão e um histórico das melhores aptidões.
        """
        population = self.generate_initial_population()
        best_solution = None
        best_fitness = 0
        fitness_history = []

        for generation in range(self.num_generations):
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

            fitness_history.append(best_fitness)

        return best_solution, best_fitness, fitness_history

    def generate_initial_population(self):
        """
        Gera a população inicial de indivíduos.

        Returns:
            list: Uma lista de indivíduos gerados aleatoriamente.
        """
        return [[random.choice([0, 1]) for _ in range(len(self.problem.items))] for _ in range(self.population_size)]

    def selection(self, population, fitness_scores):
        """
        Seleciona um indivíduo da população.

        Args:
            population (list): A população atual.
            fitness_scores (list): As pontuações de aptidão correspondentes à população.

        Returns:
            list: O indivíduo selecionado.

        Raises:
            ValueError: Se for especificado um método de seleção inválido.
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

        Args:
            population (list): A população atual.
            fitness_scores (list): As pontuações de aptidão correspondentes à população.

        Returns:
            list: O indivíduo selecionado através da seleção por torneio.
        """
        tournament = random.sample(list(zip(population, fitness_scores)), self.tournament_size)
        return max(tournament, key=lambda x: x[1])[0]

    def roulette_selection(self, population, fitness_scores):
        """
        Realiza a seleção por roleta.

        Args:
            population (list): A população atual.
            fitness_scores (list): As pontuações de aptidão correspondentes à população.

        Returns:
            list: O indivíduo selecionado através da seleção por roleta.
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
        Realiza o cruzamento entre dois pais.

        Args:
            parent1 (list): O primeiro pai.
            parent2 (list): O segundo pai.

        Returns:
            tuple: Uma tupla (crossed, child), onde crossed é um booleano indicando se ocorreu cruzamento,
                   e child é o filho resultante se ocorreu cruzamento, caso contrário None.
        """
        if random.random() < self.crossover_rate:
            crossover_point = random.randint(1, len(parent1) - 1)
            child = parent1[:crossover_point] + parent2[crossover_point:]
            return child
        else:
            return parent1.copy()

    def mutate(self, individual):
        """
        Realiza a mutação em um indivíduo.

        Args:
            individual (list): O indivíduo a ser mutado.

        Returns:
            None: O indivíduo é modificado in-place.
        """
        for i in range(len(individual)):
            if random.random() < self.mutation_rate:
                individual[i] = 1 - individual[i]  # Inverte o bit