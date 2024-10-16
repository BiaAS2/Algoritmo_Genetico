from item import Item

class KnapsackProblem:
    """
    Representa o problema da mochila, contendo itens e a capacidade da mochila.

    Esta classe fornece métodos para carregar o problema a partir de um arquivo
    e avaliar a aptidão de uma solução proposta.
    """

    def __init__(self, capacity, items):
        """
        Inicializa uma instância do problema da mochila.

        Args:
            capacity (int): A capacidade máxima da mochila.
            items (list): Uma lista de objetos Item representando os itens disponíveis.
        """
        self.capacity = capacity
        self.items = items

    def load_from_file(file_path):
        """
        Carrega os dados do problema da mochila a partir de um arquivo.

        Args:
            file_path (str): O caminho para o arquivo contendo os dados dos itens.

        Returns:
            KnapsackProblem: Uma instância de KnapsackProblem se o arquivo for carregado com sucesso.
            None: Se ocorrer um erro durante o carregamento do arquivo.

        Raises:
            FileNotFoundError: Se o arquivo especificado não for encontrado.
            ValueError: Se nenhum item válido for encontrado no arquivo.
        """
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
        """
        Avalia a aptidão de uma solução proposta para o problema da mochila.

        Esta função calcula o valor total e o peso total dos itens selecionados,
        aplicando uma penalidade se o peso exceder a capacidade da mochila.

        Args:
            solution (list): Uma lista de 0s e 1s representando a seleção de itens.
            metric (str, optional): A métrica de aptidão a ser usada. 
                Pode ser "maximize_benefit_weight" ou "maximize_benefit".
                Padrão é "maximize_benefit_weight".

        Returns:
            float: O valor de aptidão calculado para a solução proposta.

        Raises:
            ValueError: Se for especificada uma métrica de aptidão inválida.
        """
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
            excess_weight = total_weight - self.capacity
            
            for gene, item in zip(solution, self.items):
                if gene == 1 and excess_weight > 0:
                    if item.weight <= excess_weight:
                        num_excess_items += 1
                        excess_items_value += item.value
                        excess_weight -= item.weight
                    else:
                        num_excess_items += 1
                        excess_items_value += item.value * (excess_weight / item.weight)
                        break

            penalty = (num_excess_items / excess_items_value) if excess_items_value > 0 else 1
            penalty_factor = max(0, 1 - penalty)
        else:
            penalty_factor = 1

        if metric == "maximize_benefit_weight":
            fitness = (total_value / total_weight if total_weight > 0 else 0) * penalty_factor
        elif metric == "maximize_benefit":
            fitness = total_value * penalty_factor
        else:
            raise ValueError("Métrica de fitness inválida")

        return fitness