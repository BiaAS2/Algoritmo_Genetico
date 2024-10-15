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

    def evaluate_fitness(self, solution):
        total_value = sum(item.value for item, selected in zip(self.items, solution) if selected)
        total_weight = sum(item.weight for item, selected in zip(self.items, solution) if selected)
        
        if total_weight > self.capacity:
            return 0
        
        return total_value