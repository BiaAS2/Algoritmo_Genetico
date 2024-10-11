from KnapsackGA import KnapsackGA
from Plotter_Graphic import Plotter_Graphic  # Supondo que você salvou a classe em um arquivo chamado plotter.py


def main():
    ga = None

    # Parâmetros do teste (crossover, mutação, população, gerações)
    test_params = [
        (0.8, 0.1, 50, 500),
        (0.6, 0.5, 100, 1000),
        (0.7, 0.3, 75, 450),
        (0.9, 0.2, 60, 600),
        (0.5, 0.1, 80, 200),
    ]

    results = []
    results_for_plot = []  # Lista separada para armazenar o fitness_history para os gráficos

    # Instancia o algoritmo genético para ler a capacidade antes do laço
    ga = KnapsackGA(filename='instancia.csv', population_size=0, crossover_rate=0, mutation_rate=0,
                    num_generations=0)

    # Imprimir a capacidade da mochila antes do laço for
    print(f"\nCapacidade da mochila: {ga.capacity}")
    print("--------------------------------------\n")

    for i, (crossover, mutation, population_size, num_generations) in enumerate(test_params, start=1):
        ga = KnapsackGA(filename='instancia.csv', population_size=population_size, crossover_rate=crossover,
                        mutation_rate=mutation, num_generations=num_generations)

        best_solution, fitness_history = ga.run()

        # Calcule a média da aptidão após as gerações
        average_fitness = sum(fitness_history) / len(fitness_history) if fitness_history else 0
        best_fitness = max(fitness_history) if fitness_history else 0

        # Adicione os resultados à tabela do Excel
        results.append(
            (i, crossover, mutation, population_size, num_generations, average_fitness, best_fitness))

        # Adicione os resultados à lista para plotar, incluindo fitness_history
        results_for_plot.append(
            (i, crossover, mutation, population_size, num_generations, average_fitness, best_fitness, fitness_history))

        # Exibir os itens selecionados
        print(f"Teste {i} - Itens selecionados:")
        for j, item in enumerate(ga.items):
            if best_solution.genome[j] == 1:
                print(f"Item {item.name}: Peso = {item.weight}, Valor = {item.value}")
        print("--------------------------------------")

    # Salvar os resultados em um arquivo Excel
    ga.save_results_to_excel(results)

    # Criar um objeto da classe Plotter e plotar os gráficos
    plotter = Plotter_Graphic(test_params)
    plotter.plot_fitness(results_for_plot)


if __name__ == "__main__":
    main()
