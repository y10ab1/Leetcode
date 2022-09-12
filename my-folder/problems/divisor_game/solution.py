class Solution:
    def divisorGame(self, n: int) -> bool:
        # If anyone got 1, he lose
        return n%2==0