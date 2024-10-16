class Item:
    """
    Representa um item que pode ser colocado na mochila.

    Esta classe armazena informações sobre o nome, peso e valor de um item.
    """

    def __init__(self, name, weight, value):
        """
        Inicializa um novo Item.

        Args:
            name (str): O nome do item.
            weight (int): O peso do item.
            value (int): O valor do item.
        """
        self.name = name
        self.weight = weight
        self.value = value

    def __repr__(self):
        """
        Retorna uma representação em string do Item.

        Returns:
            str: Uma string representando o Item no formato "Item(name='nome', weight=peso, value=valor)".
        """
        return f"Item(name='{self.name}', weight={self.weight}, value={self.value})"
    