from Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
        self.type: str = "Creature"
        self.mana: int = 6

    def play(self, game_state: dict) -> dict:
        if super().is_playable(self.mana) is False:
            print(f"Playable: {super().is_playable(self.mana)}")
            return None
        else:
            game_state = {"card_played": self.name,
                          "mana_used": 5,
                          "effect": "creature summoned to battlefield"}
            self.mana -= 5
            return game_state

    def attack_target(self, target) -> dict:
        if not isinstance(target, str):
            print(f"{target} - invalid target")
            return None
        return {"attacker": self.name,
                'target': target,
                'damage_dealt': 7,
                'combat_resolved': True}

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self.type,
            "attack": self.attack,
            "health": self.health
        }
