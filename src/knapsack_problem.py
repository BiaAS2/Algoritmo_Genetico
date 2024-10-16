from item import Item

class KnapsackProblem:
    def __init__(self, capacity, items):
        self.capacity = capacity
        self.items = items

    @staticmethod
    def load_from_file(file_path):
        items = []
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 3:
                        name, weight, value = parts
                        items.append(Item(name, int(weight), int(value)))
                    else:
                        print(f"Ignorando linha mal formatada: {line.strip()}")
            
            if not items:
                raise ValueError("Nenhum item válido encontrado no arquivo.")
            
            capacity = sum(item.weight for item in items) // 2
            return KnapsackProblem(capacity, items)
        except FileNotFoundError:
            print(f"Arquivo não encontrado: {file_path}")
            return None
        except ValueError as e:
            print(f"Erro ao carregar arquivo: {e}")
            return None

    def evaluate_fitness(self, solution, metric="maximize_benefit_weight"):
        total_value = 0
        total_weight = 0
        excess_items_value = 0
        num_excess_items = 0

        for gene, item in zip(solution, self.items):
            if gene == 1:  # Item selecionado
                total_value += item.value
                total_weight += item.weight

        # Penalizar soluções que excedem a capacidade
        if total_weight > self.capacity:
            # Calcular o peso excedente
            excess_weight = total_weight - self.capacity
            
            # Contar itens que contribuem para o excesso
            for gene, item in zip(solution, self.items):
                if gene == 1 and excess_weight > 0:
                    if item.weight <= excess_weight:
                        num_excess_items += 1
                        excess_items_value += item.value
                        excess_weight -= item.weight
                    else:
                        # Contribuição parcial para o excesso de peso
                        num_excess_items += 1
                        excess_items_value += item.value * (excess_weight / item.weight)
                        break

            # Aplicar penalidade baseada no número de itens em excesso e seu valor total
            penalty = (num_excess_items / excess_items_value) if excess_items_value > 0 else 1
            penalty_factor = max(0, 1 - penalty)
        else:
            penalty_factor = 1  # Sem penalidade se o peso estiver dentro da capacidade

        if metric == "maximize_benefit_weight":
            # Maximizar benefício/peso
            fitness = (total_value / total_weight if total_weight > 0 else 0) * penalty_factor
        elif metric == "maximize_benefit":
            # Maximizar apenas o valor
            fitness = total_value * penalty_factor
        else:
            raise ValueError("Métrica de fitness inválida")

        return fitness