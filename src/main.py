from knapsack_problem import KnapsackProblem
from genetic_algorithm import GeneticAlgorithm

def main():
    """
    Função principal que executa o algoritmo genético para resolver o problema da mochila.
    """
    # Carregar o problema da mochila a partir de um arquivo
    problem = KnapsackProblem.load_from_file("../data/instancia.csv")

    # Imprimir informações sobre o problema carregado
    print("Problema da Mochila carregado:")
    print(f"Capacidade da mochila: {problem.capacity}")
    print(f"Número de itens: {len(problem.items)}")
    print("Primeiros 5 itens:")
    for item in problem.items[:5]:
        print(f"{item.name}: Peso = {item.weight}, Valor = {item.value}")
    print("...")

    # Parâmetros do algoritmo genético
    population_size = 100
    crossover_rate = 0.8
    mutation_rate = 0.1
    num_generations = 100
    selection_method = 'tournament'
    tournament_size = 5
    elitism = True

    # Criar e executar o algoritmo genético
    ga = GeneticAlgorithm(problem, population_size, crossover_rate, mutation_rate, num_generations, selection_method, tournament_size, elitism)
    best_solution, best_fitness = ga.run()

    # Imprimir a solução encontrada
    print("\nMelhor solução encontrada:")
    print(f"Fitness: {best_fitness}")
    print("Itens selecionados:")
    selected_items = [item for item, selected in zip(problem.items, best_solution) if selected]
    for item in selected_items[:5]:  # Mostrar apenas os primeiros 5 itens selecionados
        print(f"{item.name}: Peso = {item.weight}, Valor = {item.value}")
    
    if len(selected_items) > 5:
        print(f"... e mais {len(selected_items) - 5} item(s).")

    total_weight = sum(item.weight for item in selected_items)
    total_value = sum(item.value for item in selected_items)
    print(f"\nPeso total dos itens selecionados: {total_weight}")
    print(f"Valor total dos itens selecionados: {total_value}")
    print(f"Capacidade da mochila: {problem.capacity}")

if __name__ == "__main__":
    main()