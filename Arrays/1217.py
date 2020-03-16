class Solution:
    """
    Given an array of position indices, return the minimum cost needed to move
    all the chips to the same position (any position).

    Time: 50% (32ms) O(n)
    """
    def minCostToMoveChips(self, chips: List[int]) -> int:
        even_parity = 0
        odd_parity = 0
        for chip in chips:
            if chip % 2 == 0:
                even_parity += 1
            else:
                odd_parity += 1
        return min(even_parity, odd_parity)
