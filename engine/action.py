class Action:

    def __init__(self, relative_target=(0, 0), type="Pass"):
        self._relative_target = relative_target
        self._type = type

    @property
    def relative_target(self):
        return self._relative_target

    @property
    def type(self):
        return self._type
