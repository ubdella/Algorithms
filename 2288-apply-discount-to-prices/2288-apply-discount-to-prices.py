class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        
        def apply_discount(price):
            value = float(price[1:])
            discounted = value * (1- discount/100)
            return f'${discounted:.2f}'
        
        
        words = sentence.split()
    
        for i, word in enumerate(words):
            
            if word.startswith('$') and len(word)>1 and word[1:].isnumeric():
                words[i] = apply_discount(word)
                
                
        return ' '.join(words)
                