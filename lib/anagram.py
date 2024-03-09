# your code goes here!
# #pseudo
#     START
#         -takes in a word
#         -sort the word
#         -iterate through each letter of the word
        
#         -take in a list and iterate through each item in the list
#         -for each item, sort them.
#         -for each sorted item, iterate through  each letter of the item.
        
#         -if any of the sorted iterated item matches with the sorted iterated word, then:
#             -return the item in the return list.
#     END

# #

class Anagram:
    def __init__(self, word):
        self.word = word

    @property
    def word(self):
        return self._word

    @word.setter
    def word(self, word):
        self._word = sorted(word.lower())  # Convert to lowercase and sort characters

    def match(self, list_of_words):
        matched_anagrams = []
        for item in list_of_words:
            if sorted(item.lower()) == self.word and item.lower() != self.word:
                matched_anagrams.append(item)  # Add matching anagrams to the list
        return matched_anagrams

# Example usage:
listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))
# => ['inlets'
