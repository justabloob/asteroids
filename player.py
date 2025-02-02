class Player(CircleShape): # type: ignore
    def __init__(self, x, y):
        super().__init__(x, y)
        self.rotation = 0