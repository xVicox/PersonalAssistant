class Expense:

    def __init__(self, item_name, cost, category):
        self._item_name = item_name
        self. _cost = cost
        self._category = category

    @property
    def item_name(self):
        return self._item_name

    @property
    def cost(self):
        return self._cost

    @property
    def category(self):
        return self._category

    def __str__(self):
        return (f"Item: {self._item_name}\n"
                f"Cost: {self._cost:.2f}\n"
                f"Category: {self._category}")

