import random

class GeneticAlgorithm:
    """
    Implementa um algoritmo genético para resolver o problema da mochila.

    Esta classe fornece métodos para executar o algoritmo genético, incluindo
    seleção, cruzamento e mutação de indivíduos em uma população.
    """

    def __init__(self, problem, population_size, crossover_rate, mutation_rate, num_generations, selection_method='tournament', tournament_size=5, elitism=False, fitness_metric="maximize_benefit_weight"):
        """
        Inicializa uma instância do algoritmo genético.

        Args:
            problem (KnapsackProblem): O problema da mochila a ser resolvido.
            population_size (int): O tamanho da população em cada geração.
            crossover_rate (float): A taxa de cruzamento (probabilidade de cruzamento).
            mutation_rate (float): A taxa de mutação (probabilidade de mutação por gene).
            num_generations (int): O número de gerações a serem executadas.
            selection_method (str, optional): O método de seleção ('tournament' ou 'roulette'). Padrão é 'tournament'.
            tournament_size (int, optional): O tamanho do torneio para o método de seleção por torneio. Padrão é 5.
            elitism (bool, optional): Se True, preserva o melhor indivíduo em cada geração. Padrão é False.
            fitness_metric (str, optional): A métrica de aptidão a ser usada. Padrão é "maximize_benefit_weight".
        """
        self.problem = problem
        self.population_size = population_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.num_generations = num_generations
        self.selection_method = selection_method
        self.tournament_size = tournament_size
        self.elitism = elitism
        self.fitness_metric = fitness_metric

    def run(self):
        """
        Executa o algoritmo genético.

        Returns:
            tuple: Uma tupla contendo a melhor solução encontrada, sua aptidão e um histórico de aptidões.
        """
        population = self.generate_initial_population()
        best_solution = None
        best_fitness = 0
        fitness_history = []

        for generation in range(self.num_generations):
            fitness_scores = [self.problem.evaluate_fitness(individual, metric=self.fitness_metric) for individual in population]
            
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
        Gera a população inicial aleatoriamente.

        Returns:
            list: Uma lista de indivíduos, cada um representando uma solução potencial.
        """
        return [[random.choice([0, 1]) for _ in range(len(self.problem.items))] for _ in range(self.population_size)]

    def selection(self, population, fitness_scores):
        """
        Seleciona um indivíduo da população usando o método de seleção especificado.

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
            raise ValueError("Método de seleção inválido")

    def tournament_selection(self, population, fitness_scores):
        """
        Realiza a seleção por torneio.

        Args:
            population (list): A população atual.
            fitness_scores (list): As pontuações de aptidão correspondentes à população.

        Returns:
            list: O indivíduo vencedor do torneio.
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
            list: O indivíduo selecionado pela roleta.
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
            list: O filho resultante do cruzamento.
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