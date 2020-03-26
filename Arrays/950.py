from collections import deque
class Solution:
    """
    Time: 99% (28ms)
    """
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        sim_deck = deque(range(len(deck)))
        sorted_deck = sorted(deck)
        indices = []
        result = [0] * len(deck)
        while len(sim_deck) > 0:
            indices.append(sim_deck.popleft())
            sim_deck.rotate(-1)
        for i in range(len(deck)):
            result[indices[i]] = sorted_deck[i]
        return result
