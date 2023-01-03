"""dollar通貨
"""


class Dollar:
    """ドル通貨を表す
    """

    def __init__(self, amount: int):
        """初期化

        Args:
            amount (int): _description_
        """
        self.amount = amount
        # self.amount = 10

    def times(self, multiplier: int):
        """通貨交換

        Args:
            multiplier (int): _description_
        """
        return Dollar(self.amount * multiplier)
