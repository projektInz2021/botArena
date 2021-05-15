from map import Map
from bot import Bot


class Engine:
    def __init__(self):
        self._map = Map()
        self._bots = []

    def register_bot(self, token):
        self._bots.append(Bot(token))

    def start(self):
        self._spawn_bots()

    def tick(self):

        pass

    def _spawn_bots(self):
        for bot in self._bots:
            spawnpoint = self._map.get_available_spawnpoint()
            bot.set_position(spawnpoint)

    def _perform_bot_action(self, token, action):
        for bot in self._bots:
            if token == bot.token:
                if action.type == "Move":
                    self._map.move_by(bot, action.relative_target)
                elif action.type == "Plant":
                    self._map.plant_bomb(action.relative_target)

    def _update_map(self):

        pass
