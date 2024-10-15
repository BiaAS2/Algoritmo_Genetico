class Item:
    """
    Representa um item que pode ser colocado na mochila.

    Atributos:
        name (str): O nome do item.
        weight (int): O peso do item.
        value (int): O valor do item.
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
            str: Uma string representando o Item.
        """
        return f"Item(name='{self.name}', weight={self.weight}, value={self.value})"