class Candidate:
    def __init__(self, genome):
        self.genome = genome
        self.fitness = 0

    def calculate_fitness(self, items, capacity, metric="maximize_benefit_weight"):
        total_value = 0
        total_weight = 0
        excess_items_value = 0
        num_excess_items = 0

        for gene, item in zip(self.genome, items):
            if gene == 1:  # Item selecionado
                total_value += item.value
                total_weight += item.weight

        # Penalizar soluções que excedem a capacidade
        if total_weight > capacity:
            # Calculate the excess weight
            excess_weight = total_weight - capacity
            
            # Count items contributing to excess
            for gene, item in zip(self.genome, items):
                if gene == 1 and excess_weight > 0:
                    if item.weight <= excess_weight:
                        num_excess_items += 1
                        excess_items_value += item.value
                        excess_weight -= item.weight
                    else:
                        # Partial contribution to excess weight
                        num_excess_items += 1
                        excess_items_value += item.value * (excess_weight / item.weight)
                        break

            # Apply penalty based on the number of excess items and their total value
            penalty = (num_excess_items / excess_items_value) if excess_items_value > 0 else 1
            penalty_factor = max(0, 1 - penalty)
        else:
            penalty_factor = 1  # No penalty if weight is within capacity

        if metric == "maximize_benefit_weight":  # Maximizar benefício/peso
            self.fitness = (total_value / total_weight if total_weight > 0 else 0) * penalty_factor
        elif metric == "maximize_benefit":  # Maximizar apenas o valor
            self.fitness = total_value * penalty_factor

        return self.fitness

