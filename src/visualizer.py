import matplotlib.pyplot as plt 

class Visualizer:
    def __init__(self, test_params):
        self.test_params = test_params

    def plot_fitness(self, results):
        """Plota a evolução da melhor solução em gráficos separados."""
        num_tests = len(results)
        cols = 2  # Número de colunas
        rows = (num_tests + 1) // cols  # Número de linhas necessário

        fig, axes = plt.subplots(rows, cols, figsize=(12, 8))
        axes = axes.flatten()  # Facilita o acesso aos eixos

        for i, result in enumerate(results):
            test_num, crossover, mutation, population_size, num_generations, average_fitness, best_fitness, fitness_history = result
            axes[i].plot(fitness_history, label=f'Teste {test_num} (Crossover: {crossover}, Mutação: {mutation})')
            axes[i].set_title(f'Teste {test_num}')
            axes[i].set_xlabel('Gerações')
            axes[i].set_ylabel('Melhor Fitness')
            axes[i].legend()

        # Se houver gráficos não utilizados, oculte-os
        for j in range(i + 1, len(axes)):
            fig.delaxes(axes[j])

        # Ajustar layout
        plt.tight_layout()
        plt.show()
