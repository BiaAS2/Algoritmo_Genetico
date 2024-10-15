import matplotlib.pyplot as plt
from knapsack_problem import KnapsackProblem
from genetic_algorithm import GeneticAlgorithm
import numpy as np
import math

def run_test(problem, population_size, crossover_rate, mutation_rate, num_generations, selection_method, tournament_size, elitism, num_runs=5):
    results = []
    histories = []
    for _ in range(num_runs):
        ga = GeneticAlgorithm(problem, population_size, crossover_rate, mutation_rate, num_generations, selection_method, tournament_size, elitism)
        _, best_fitness, fitness_history = ga.run()
        results.append(best_fitness)
        histories.append(fitness_history)
    return np.mean(results), np.mean(histories, axis=0)

def test_and_plot(problem, test_params):
    num_tests = len(test_params)
    rows = 5
    cols = 3
    
    plt.figure(figsize=(15, 10))

    for i, params in enumerate(test_params, 1):
        population_size, crossover_rate, mutation_rate, num_generations, selection_method, tournament_size = params
        
        result_with, history_with = run_test(problem, population_size, crossover_rate, mutation_rate, num_generations, selection_method, tournament_size, True)
        result_without, history_without = run_test(problem, population_size, crossover_rate, mutation_rate, num_generations, selection_method, tournament_size, False)
        
        plt.subplot(rows, cols, i)
        plt.plot(history_with, label='Com Elitismo')
        plt.plot(history_without, label='Sem Elitismo')
        plt.title(f"Teste {i}: {selection_method.capitalize()}\nPop: {population_size}, CR: {crossover_rate}, MR: {mutation_rate}, Gen: {num_generations}")
        plt.xlabel('Geração')
        plt.ylabel('Fitness')
        plt.legend()

        print(f"Teste {i}:")
        print(f"  Método de Seleção: {selection_method}")
        print(f"  Tamanho da População: {population_size}")
        print(f"  Taxa de Cruzamento: {crossover_rate}")
        print(f"  Taxa de Mutação: {mutation_rate}")
        print(f"  Número de Gerações: {num_generations}")
        if selection_method == 'tournament':
            print(f"  Tamanho do Torneio: {tournament_size}")
        print(f"  Fitness Médio com Elitismo: {result_with}")
        print(f"  Fitness Médio sem Elitismo: {result_without}")
        print()

    plt.tight_layout()
    plt.show()

def main():
    problem = KnapsackProblem.load_from_file("../data/instancia.csv")
    if problem is None:
        print("Não foi possível carregar o problema. Encerrando o programa.")
        return

    test_params = [
        # Testes com Tournament
        (100, 0.7, 0.01, 100, 'tournament', 3),
        (200, 0.75, 0.05, 150, 'tournament', 5),
        (150, 0.8, 0.1, 200, 'tournament', 4),
        (250, 0.85, 0.03, 120, 'tournament', 6),
        (180, 0.9, 0.08, 180, 'tournament', 5),
        # Testes com Roulette
        (100, 0.7, 0.01, 100, 'roulette', None),
        (200, 0.75, 0.05, 150, 'roulette', None),
        (150, 0.8, 0.1, 200, 'roulette', None),
        (250, 0.85, 0.03, 120, 'roulette', None),
        (180, 0.9, 0.08, 180, 'roulette', None)
    ]

    test_and_plot(problem, test_params)

if __name__ == "__main__":
    main()