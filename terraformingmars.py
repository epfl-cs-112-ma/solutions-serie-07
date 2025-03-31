from __future__ import annotations

from abc import abstractmethod
from enum import Enum, auto

# Il y a évidemment plein de solutions possibles. L'énoncé est
# intentionnellement très vague sur beaucoup de points, afin de vous laisser
# explorer diverses idées.

# --- Badges ---

class BadgeKind(Enum):
    EXAMPLE = auto()

class BadgeProvider:
    @abstractmethod
    def count_badges(self, kind: BadgeKind) -> int: ...

    def has_badge(self, kind: BadgeKind) -> bool:
        return self.count_badges(kind) > 0

# --- Powers ---

class Power: pass

class OnPlayCardPower(Power):
    @abstractmethod
    def on_play_card_with_badges(self, card: CardWithBadges, cost: int) -> int:
        """Executed when the player plays a card.

        The incoming cost of the card is `cost`. The method should return the
        adjusted cost based on its power. For example, if it reduces the cost
        of the card by 2 M€, it should return `cost - 2`.
        """
        ...

class OnPlaceCityPower(Power):
    @abstractmethod
    def on_place_city(self, city_owner: Corporation) -> None: ...

class NoPower(Power):
    """A fake Power for corporations that have no permanent power."""
    pass

# --- Cards ---

class Card: pass

class CardWithBadges(Card, BadgeProvider): pass

class GreenCard(CardWithBadges): pass
class BlueCard(CardWithBadges, Power): pass
class RedCard(Card): pass

# --- Corporations ---

class Corporation(BadgeProvider, Power):
    def receive_money(self, amount: int) -> None: ...
    def increase_energy_production(self, amount: int) -> None: ...
