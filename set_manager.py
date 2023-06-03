class SetManager:
    def __init__(self, regular_manager):
        self.regular_manager = regular_manager

    def __iter__(self):
        return iter(set.union(*(obj.top_players_set for obj in self.regular_manager.game_list)))

    def __len__(self):
        return sum(len(obj.top_players_set) for obj in self.regular_manager.game_list)

    def __getitem__(self, index):
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        for obj in self.regular_manager.game_list:
            players = obj.top_players_set
            if index < len(players):
                return list(players)[index]
            index -= len(players)
        raise IndexError("Index out of range")

    def __next__(self):
        if not hasattr(self, "_iterator"):
            self._iterator = iter(self)
        return next(self._iterator)
