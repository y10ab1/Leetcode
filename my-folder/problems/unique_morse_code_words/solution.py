class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse_dict = defaultdict(str)
        for i,m in enumerate(table):
            morse_dict[ord('a')+i] = m
        
        trans = {}
        t = ""
        for word in words:
            for c in word:
                t+=morse_dict[ord(c)]
            trans[t] = 1
            t = ""
        return len(trans)