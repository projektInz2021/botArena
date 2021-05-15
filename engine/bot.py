class Bot:
    def __init__(self, token):
        self._token = token

        self._position = (0, 0)
        self._cooldown = 0

    @property
    def token(self):
        return self._token

    def set_position(self, position):
        self._position = position

    def reduce_cooldown(self):
        if self._cooldown > 0:
            self._cooldown -= 1
