# Trabalho Prático - Problema da Mochila

## Descrição do Projeto

Este projeto implementa um Algoritmo Genético para resolver o Problema da Mochila, que consiste em determinar a melhor combinação de itens a serem incluídos na mochila, respeitando a capacidade da mochila.

## Funcionalidades

- Leitura das instâncias a partir de arquivos CSV;
- As seleções são feitas por TORNEIO e ROLETA;
- Operadores de CRUZAMENTO e MUTAÇÃO;
- Penalização na função de fitness caso exceda o limite de peso.

## Métodos Implementados:

- **Torneio**: O método de seleção por torneio seleciona aleatoriamente um grupo de indivíduos e escolhe o melhor entre eles, repetindo o processo para criar uma nova população.
- **Roleta**: A seleção por roleta seleciona indivíduos de acordo com sua fitness relativa. Indivíduos com melhor fitness têm maior probabilidade de serem escolhidos.
- **Cruzamento**: O cruzamento é feito combinando genes de dois pais para gerar dois novos indivíduos. Foram testadas variações com cruzamento de ponto único.
- **Mutação**: A mutação altera aleatoriamente os genes de alguns indivíduos para manter a diversidade da população. Testamos diferentes taxas de mutação.
- **Penalização na Função de Fitness**: A penalização foi aplicada para que, quando o peso total dos itens ultrapassasse o limite da mochila, a solução fosse penalizada proporcionalmente ao excesso de peso.

## Testes e Resultados

Foram realizados diversos testes variando os parâmetros de entrada do algoritmo, como taxa de cruzamento, taxa de mutação, tamanho da população e número de gerações. O desempenho foi medido tanto em termos de benefício total quanto na razão benefício/peso.

Além disso, realizamos testes comparando os resultados **com** e **sem elitismo**, e observamos uma melhora significativa no tempo de convergência quando o elitismo foi aplicado.

### Gráficos das Evoluções

![Gráficos](./img/)

## Conclusão

Com base nos testes realizados, o algoritmo genético foi eficaz em encontrar soluções de alta qualidade para o problema da mochila. O uso de elitismo mostrou uma melhora significativa na convergência, enquanto diferentes taxas de cruzamento e mutação tiveram um impacto importante na diversidade das soluções.

---

### Trabalho desenvolvido por:

**Grupo**:

- [Beatriz Alves](https://www.linkedin.com/in/beatriz-alves-de-souza-789a84239/)
- [Bianca Mayra](https://www.linkedin.com/in/bianca-mayra-de-assisaguiar-8b18b0235/)
- [Luana]()
- [Lucelho Silva](https://www.linkedin.com/in/lucelhosilva/)
- [Renato Noronha](https://www.linkedin.com/in/renatonoronha/)
- [Túlio Inácio](https://www.linkedin.com/in/t%C3%BAlio-in%C3%A1cio-767244276/)

Data: **25 de outubro de 2024**

## Docente do Projeto

Glender Brás | [Linkedin](https://www.linkedin.com/in/glenderbras/)
