from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        if super().is_playable(self.mana) is False:
            print(f"Playable: {super().is_playable(self.mana)}")
            return None
        else:
            game_state = {"card_played": self.name,
                          "mana_used": self.cost,
                          "effect": f"{self.effect_type} spell cast"}
            return game_state

    def resolve_effect(self, targets: list) -> dict:
        if not isinstance(targets, list):
            print(f"Invalid targets: {targets}")
            return None
        return {"spell": self.name,
                "effect_type": self.effect_type,
                "targets": targets,
                "effect_resolved": True}
