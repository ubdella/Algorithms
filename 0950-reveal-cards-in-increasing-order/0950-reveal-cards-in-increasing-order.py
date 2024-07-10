class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse = True)
        
        revealed = deque()
        
        for card in deck:
            if revealed:
                revealed.appendleft(revealed.pop())
                
            revealed.appendleft(card)
            
        return list(revealed)