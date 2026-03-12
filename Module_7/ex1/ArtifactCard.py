from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.type: str = "Artifact"
        self.mana: int = 4

    def play(self, game_state: dict) -> dict:
        if super().is_playable(self.mana) is False:
            print(f"Playable: {super().is_playable(self.mana)}")
            return None
        else:
            game_state = {"card_played": self.name,
                          "mana_used": self.cost,
                          "effect": self.effect}
            self.mana -= self.cost
            return game_state

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self.type,
            "durability": self.durability,
            "effect": self.effect
        }
