# lib/anagram.py

class Anagram:
    def __init__(self, word):
        # Store the original word and a sorted version for comparison
        self.word = word
        self.sorted_word = sorted(word)

    def match(self, word_list):
        matches = []

        for candidate in word_list:
            # Check if sorted letters match, and exclude exact same word (optional)
            if sorted(candidate) == self.sorted_word and candidate.lower() != self.word.lower():
                matches.append(candidate)

        return matches

