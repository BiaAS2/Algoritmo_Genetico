class Individual:
    def __init__(self, genome):
        self.genome = genome
        self.fitness = 0

    def calculate_fitness(self, items, capacity, metric="maximize_benefit_weight"):
        total_value = 0
        total_weight = 0

        for gene, item in zip(self.genome, items):
            if gene == 1:  # Item selecionado
                total_value += item.value
                total_weight += item.weight

        # Penalizar soluções que excedem a capacidade
        if total_weight > capacity:
            self.fitness = 0
        else:
            if metric == "maximize_benefit_weight":  # Maximizar benefício/peso
                self.fitness = total_value / total_weight if total_weight > 0 else 0
            elif metric == "maximize_benefit":  # Maximizar apenas o valor
                self.fitness = total_value
        return self.fitness

