class Anagram:
    def __init__(self, word: str):
        self.word = word
        
    @property
    def word(self):
        return self._word
    
    @word.setter
    def word(self, word: str):
        if isinstance(word, str):
            self._word = word
        else:
            print("Anagram requires a string in order to evaluate its anagrams.")
        
    def match(self, word_list: list):
        match_list = []
        
        for word in word_list:
            if len(word) == len(self._word):
                if sorted(word.lower()) == sorted(self.word.lower()):
                    match_list.append(word)
                
        return match_list