from item import Item

class KnapsackProblem:
    """
    Representa o problema da mochila.

    Atributos:
        capacity (int): A capacidade máxima da mochila.
        items (list): Uma lista de objetos Item disponíveis para serem colocados na mochila.
    """

    def __init__(self, capacity, items):
        """
        Inicializa uma nova instância do problema da mochila.

        Args:
            capacity (int): A capacidade máxima da mochila.
            items (list): Uma lista de objetos Item disponíveis.
        """
        self.capacity = capacity
        self.items = items

    @staticmethod
    def load_from_file(file_path):
        """
        Carrega uma instância do problema da mochila a partir de um arquivo.

        Args:
            file_path (str): O caminho para o arquivo contendo os dados do problema.

        Returns:
            KnapsackProblem: Uma nova instância do problema da mochila.
        """
        with open(file_path, 'r') as file:
            capacity = int(file.readline().strip())
            num_items = int(file.readline().strip())
            items = []
            for _ in range(num_items):
                name, weight, value = file.readline().strip().split(',')
                items.append(Item(name, int(weight), int(value)))
        return KnapsackProblem(capacity, items)

    def evaluate_fitness(self, solution):
        """
        Avalia a aptidão (fitness) de uma solução para o problema da mochila.

        Args:
            solution (list): Uma lista de 0s e 1s representando quais itens estão na mochila.

        Returns:
            int: O valor total dos itens na mochila, ou 0 se o peso exceder a capacidade.
        """
        total_value = sum(item.value for item, selected in zip(self.items, solution) if selected)
        total_weight = sum(item.weight for item, selected in zip(self.items, solution) if selected)
        
        if total_weight > self.capacity:
            return 0
        
        return total_value

    def evaluate_cost_benefit(self, solution):
        """
        Calcula a relação custo-benefício de uma solução para o problema da mochila.

        Args:
            solution (list): Uma lista de 0s e 1s representando quais itens estão na mochila.

        Returns:
            float: A relação valor/peso dos itens na mochila, ou 0 se o peso exceder a capacidade.
        """
        total_value = sum(item.value for item, selected in zip(self.items, solution) if selected)
        total_weight = sum(item.weight for item, selected in zip(self.items, solution) if selected)
        
        if total_weight > self.capacity:
            return 0
        
        return total_value / total_weight if total_weight > 0 else 0